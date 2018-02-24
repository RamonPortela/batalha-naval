from navio import Navio
from jogador import Jogador
import socket
from threading import Thread
import multiprocessing
import time
import pickle

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
totalNaviosPorJogador = 10

jogadores = {}

def esperaConexao(idJogador):
    socket_jogador, addr_jogador = socket_servidor.accept()
    jogadores[idJogador] = (socket_jogador, addr_jogador, Jogador(idJogador))
    jogadores[idJogador][socket].send(msgAguardando.encode('ascii'))
    print('conexão recebida do ip: ' + jogadores[idJogador][addr][ip] + ':' + str(jogadores[idJogador][addr][porta]))

def esperarCriacaoNavios(tupla):
    a = jogadores[tupla][jogador].navios

    while len(jogadores[tupla][jogador].navios) < totalNaviosPorJogador:
        b = jogadores[tupla][socket].recv(1024)
        navio = pickle.loads(b)
        #verificar se o navio está numa posição válida
        jogadores[tupla][jogador].navios.append(navio)
        print(len(jogadores[tupla][jogador].navios))
        jogadores[tupla][socket].send(pickle.dumps(true))
    
    print("Jogador " + str(tupla) + "terminou de posicionar os navios.")

esperaConexao(jogadorUm)
esperaConexao(jogadorDois)

print("Preparando para iniciar a partida")

for j in jogadores.values():
    j[socket].send(msgIniciando.encode('ascii'))

t1 = Thread(target=esperarCriacaoNavios, args=(jogadorUm,))
t2 = Thread(target=esperarCriacaoNavios, args=(jogadorDois,))

t1.start()
t2.start()


#print(navios)
