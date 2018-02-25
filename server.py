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
msgAguardandoNavios = "Aguardando o outro jogador terminar de posicionar seus navios"
msgNaviosPosicionados = 'Navios posicionados, iniciando partida'

jogadorUm = 1
jogadorDois = 2
socket = 0
addr = 1
jogador = 2
ip = 0
porta = 1
totalNaviosPorJogador = 10
tamanhoResposta = 1024

jogadores = {}

def esperaConexao(idJogador):
    socket_jogador, addr_jogador = socket_servidor.accept()
    jogadores[idJogador] = (socket_jogador, addr_jogador, Jogador(idJogador))
    enviarMensagemParaJogador(idJogador, msgAguardando)
    print('conexão recebida do ip: ' + jogadores[idJogador][addr][ip] + ':' + str(jogadores[idJogador][addr][porta]))

def esperarCriacaoNavios(idJogador):
    while len(jogadores[idJogador][jogador].navios) < totalNaviosPorJogador:
        b = jogadores[idJogador][socket].recv(tamanhoResposta)
        linha, coluna, navio = pickle.loads(b)
        posicaoValida = jogadores[idJogador][jogador].setNavioInCampo(linha, coluna, navio.direcao, navio.tamanho)
        if posicaoValida:
            jogadores[idJogador][jogador].navios.append(navio)

        enviarMensagemParaJogador(idJogador, posicaoValida)
    
    enviarMensagemParaJogador(idJogador, msgAguardandoNavios)
    print("Jogador " + str(idJogador) + " terminou de posicionar os navios.")

def enviarMensagemParaAmbosJogadores(mensagem):
    if type(mensagem) is str:
        for j in jogadores.values():
            j[socket].send(mensagem.encode('ascii'))
    else:
        for j in jogadores.values():
            msgBytes = pickle.dumps(mensagem)
            j[socket].send(msgBytes)

def enviarMensagemParaJogador(idJogador, mensagem):
    if type(mensagem) is str:
        jogadores[idJogador][socket].send(mensagem.encode('ascii'))
    else:
        msgBytes = pickle.dumps(mensagem)
        jogadores[idJogador][socket].send(msgBytes)

def executarRodada(idJogadorVez, idJogadorEsperando):
    enviarMensagemParaJogador(idJogadorVez, True)
    enviarMensagemParaJogador(idJogadorEsperando, False)
    envioJogador = jogadores[idJogadorVez][socket].recv(tamanhoResposta)
    linha, coluna = pickle.loads(envioJogador)
    acertou = jogadores[idJogadorVez].verificarSeTiroAcertou(linha, coluna)

    if acertou:
        enviarMensagemParaAmbosJogadores(True)
    else:
        enviarMensagemParaAmbosJogadores(False)

esperaConexao(jogadorUm)
esperaConexao(jogadorDois)

print("Preparando para iniciar a partida")

enviarMensagemParaAmbosJogadores(msgIniciando)

t1 = Thread(target=esperarCriacaoNavios, args=(jogadorUm,))
t2 = Thread(target=esperarCriacaoNavios, args=(jogadorDois,))

t1.start()
t2.start()

t1.join()
t2.join()

print(msgNaviosPosicionados)
enviarMensagemParaAmbosJogadores(msgNaviosPosicionados)

turno = jogadorUm
envioJogador = None

while True:
    if turno == jogadorUm:
        executarRodada(jogadorUm, jogadorDois)
        turno = jogadorDois
    else:
        executarRodada(jogadorDois, jogadorUm)
        turno = jogadorUm

jogadores[jogadorUm][socket].close()
jogadores[jogadorDois][socket].close()
