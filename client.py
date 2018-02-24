import socket

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 12397))