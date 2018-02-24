from navio import Navio
from jogador import Jogador
import socket
from threading import Thread
import multiprocessing
import time

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
jogador = 2
ip = 0
porta = 1
navios = []

jogadores = {}

def esperaConexao(idJogador):
    socket_jogador, addr_jogador = socket_servidor.accept()
    jogadores[idJogador] = (socket_jogador, addr_jogador, Jogador(idJogador))
    jogadores[idJogador][socket].send(msgAguardando.encode('ascii'))
    print('conexão recebida do ip: ' + jogadores[idJogador][addr][ip] + ':' + str(jogadores[idJogador][addr][porta]))

def esperarCriacaoNavios(tupla):
    print(tupla)
    #idJogador = int(tupla[0])
    while len(jogadores[tupla][jogador].navios) != 10:
        pass

esperaConexao(jogadorUm)
esperaConexao(jogadorDois)

print("Preparando para iniciar a partida")

for jogador in jogadores.values():
    jogador[socket].send(msgIniciando.encode('ascii'))

t1 = Thread(target=esperarCriacaoNavios, args=(jogadorUm,))
t2 = Thread(target=esperarCriacaoNavios, args=(jogadorDois,))

t1.start()
t2.start()


print(navios)
