#
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8081))


count = 0
while True:
    count += 1
    data = input("请输入数据")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说:"+info.decode("utf-8"))
    if count > 10:
        client.close()
