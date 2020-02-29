import socket


UDPServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

UDPServer.bind(("localhost", 8082))
print("服务器启动成功。。。")
while True:
    data,address = UDPServer.recvfrom(1024)
    print(address,"说：",data.decode("utf-8"))

    # 服务器给客户端发消息
    toCliet = input("发给客户端的数据是：")
    UDPServer.sendto(toCliet.encode("utf-8"),address)
