import time
import zmq

"""
ZeroMQのPubとSub
server262.pyで送信
client262.pyで受信
接続したタイミングだけリアルタイムで受け取る
"""

context = zmq.Context()
# sock = context.socket(zmq.PUSH)
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5690")

id = 0
while True:
    id += 1
    sock.send(('sub1:' + str(id)).encode())
    print("Sent: {}".format(id))
    time.sleep(1)