"""
celeryでタスクを非同期で実行する

インストール
$ brew install rabbitmq
パス
/usr/local/sbin/rabbitmq-server
起動
$ rabbitmq-server start

celeryインストール
$ pip3 install celery

$ celery -A tasks worker --loglevel=info
"""

import time
import random

import celery

app = celery.Celery(
    'tasks',
    broker='amqp://guest@localhost',
    backend='amqp://guest@localhost'
)

# デコレーター
@app.task
def build_server():
    print('wait 10 sec')
    time.sleep(10)
    server_id = random.randint(1, 100)
    return server_id

# グルーピング
@app.task
def build_servers():
    g = celery.group(
        build_server.s() for _ in range(10))
    return g()

# コールバック
@app.task
def callback(result):
    for server_id in result:
        print(server_id)
    print('clean up')
    return 'done'

@app.task
def build_servers_with_cleanup():
    c = celery.chord(
        (build_server.s() for _ in range(10)),
        callback.s())
    return c()

@app.task
def setup_dns(server_id):
    print('setup dins for {}'.format(server_id))
    return 'done for {}'.format(server_id)

@app.task
def deploy_customer_server():
    chain = build_server.s() | setup_dns.s()
    return chain()