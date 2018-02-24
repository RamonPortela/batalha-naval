from navio import Navio
from jogador import Jogador
import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= "localhost"
porta = 12397
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("esperando jogadores...")

jogadores = {}

jogadorId = 1

jogadores[jogadorId] = (socket_servidor.accept(), Jogador(jogadorId))

print(jogadores)