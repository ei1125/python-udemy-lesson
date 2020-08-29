"""
"""
import tasks

# 非同期で実行
# result = tasks.build_server.delay()
# result = tasks.build_servers.delay()
# result = tasks.build_servers_with_cleanup.delay()
result = tasks.deploy_customer_server.delay()

# result = tasks.build_server()
print('doing...')
print(result)