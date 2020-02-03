#!/usr/bin/python3
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))


for users in [b'zhangs',b'lisi',b'wangwu',b'zhangs',b'lisi',b'wangwu',b'zhangs',b'lisi',b'wangwu']:
    s.send(users)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
