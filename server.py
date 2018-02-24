from navio import Navio
from jogador import Jogador
import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= "localhost"
porta = 12397
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("esperando jogadores...")

msgAguardando = "Aguardando outro jogador..."
msgIniciando = "Iniciando partida!"

jogadorUm = 1
jogadorDois = 2
socket = 0
addr = 1
ip = 0
porta = 1

jogadores = {}

def esperaConexao(idJogador):
    socket_jogador, addr_jogador = socket_servidor.accept()
    jogadores[idJogador] = (socket_jogador, addr_jogador, Jogador(idJogador))
    jogadores[idJogador][socket].send(msgAguardando.encode('ascii'))
    print('conexão recebida do ip: ' + jogadores[idJogador][addr][ip] + ':' + str(jogadores[idJogador][addr][porta]))

esperaConexao(jogadorUm)
esperaConexao(jogadorDois)

print("Preparando para iniciar a partida")

for jogador in jogadores.values():
    jogador[socket].send(msgIniciando.encode('ascii'))

