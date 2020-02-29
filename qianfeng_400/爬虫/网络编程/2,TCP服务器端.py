import socket



# 使用socket模块
# 创建socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定
server.bind(("localhost",8081))
# 监听
server.listen(5)
print("服务器启动成功")

#等待链接
clientSocket,clientAddress = server.accept()
print("%s---%s"%(str(clientSocket),clientAddress))

while True:
    data = clientSocket.recv(1024)
    print("收到的数据:"+data.decode("utf-8"))
    clientSocket.send("你也好坏".encode("utf-8"))