import time
import zmq

"""
ZeroMQのPushとPull
client261.pyで受信
$ python3 client261.py
を叩くと動き出す
"""

context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:5690")

id = 0
while True:
    id += 1
    sock.send(str(id).encode())
    print("Sent: {}".format(id))
    time.sleep(1)