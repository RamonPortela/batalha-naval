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

socket_jogador, addr_jogador = socket_servidor.accept()

jogadores[jogadorId] = (socket_jogador, addr_jogador, Jogador(jogadorId))
jogadores[1][0].send('oi do servidor'.encode('ascii'))

print(jogadores)