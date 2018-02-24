import socket
#from playsound import playsound

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 12397))

msg=s.recv(1024)
print(msg.decode('ascii'))

msg=s.recv(1024)
print(msg.decode('ascii'))
