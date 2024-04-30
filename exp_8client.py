import socket
Server_ip="localhost"
Server_host=8002
FORMAT="utf-8"
CS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CS.connect((Server_ip,Server_host))
file = open(r"C:\Users\anush\OneDrive\Desktop\mc\data.txt","r")
data=file.read()
CS.send("abc.txt".encode(FORMAT))
msg=CS.recv(1024)
print(msg)
CS.send(data.encode(FORMAT))
msg=CS.recv(1024)
print(msg)
