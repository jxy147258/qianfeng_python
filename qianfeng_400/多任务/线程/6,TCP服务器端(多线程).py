import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",8081))
server.listen(5)
print("服务器启动成功")

def run(ck):
    data = clientSocket.recv(1024)
    print("收到的数据:" + data.decode("utf-8"))
    clientSocket.send("你也好坏".encode("utf-8"))

while True:
    clientSocket, clientAddress = server.accept()
    # print("%s---%s" % (str(clientSocket), clientAddress))
    t = threading.Thread(target=run,args=(clientSocket,))
    t.start()


'''

    data = clientSocket.recv(1024)
    print("收到的数据:"+data.decode("utf-8"))
    clientSocket.send("你也好坏".encode("utf-8"))
'''