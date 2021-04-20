import socket

s = socket.socket() #Socket created

s.bind(('localhost', 9999))

s.listen(0)
print("waiting for connection")

clisoc, addr = s.accept()
print("Connnection established")
name = clisoc.recv(1024).decode()
print("user name recieved")    
print('connected with ', addr)
print("user : " + name)
clisoc.send(bytes('Welcome to \'localhost\'', 'utf-8'))
print("welcome message sent to client\n")
s.close()