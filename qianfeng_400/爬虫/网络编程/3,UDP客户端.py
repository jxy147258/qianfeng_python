import socket



UDPClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input("请输入数据：")
    UDPClient.sendto(data.encode("utf-8"),("localhost",8082))
    # 接受服务器的消息
    info = UDPClient.recv(1024).decode("utf-8")
    print("服务器说：",info)
