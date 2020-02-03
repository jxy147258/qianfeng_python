#!/usr/bin/python3
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('waiting for connnection....')


def tcplink(sock, addr):
    print('new connection is %s:%s' % addr)
    sock.send(b'welcome to server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello %s' % data.decode('utf-8')).encode('utf-8'))
    s.close()
    print('connection from %s:%s is end' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()




