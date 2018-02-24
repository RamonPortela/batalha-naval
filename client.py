import pickle
import socket
from navio import Navio
import time

tiros = {}
matriz = [[0] * 10] * 10

navios = {1: Navio('Porta-Avião', 5, None), 2: Navio('Navio-Tanque', 4, None), 3: Navio('Navio-Tanque', 4, None), 4: Navio('Contra Torpedeiro', 3, None), 5: Navio('Contra Torpedeiro', 3, None), 6: Navio('Contra Torpedeiro', 3, None), 7: Navio('Submarino', 2, None), 8: Navio('Submarino', 2, None), 9: Navio('Submarino', 2, None), 10: Navio('Submarino', 2, None)}

def desenharMatriz():
    print("   ", " ".join([str(a) for a in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    print("   ", "_".join(["_"] * 10))
    x = 0
    for linha in matriz:
        print(x, "|", ' '.join([str(a) for a in linha]))
        x+=1

def atirar():
    tupla = executarTiro()
    s.send(tupla)
    msg = s.recv(1024)
    #tem que converter
    
    if msg == 'acertou':
        matriz[tupla[0]][tupla[1]] = 'X'
        print("Opa fion, acertou")
    elif msg == "errou":
        matriz[tupla[0]][tupla[1]] = '~'
        print("Errou!!!!")
    else:
        print("winner winner chicken dinner")

    desenharMatriz()



def validarEntrada(entrada):
    return entrada > 0 and entrada < 9

def executarTiro():
    while True:
        linha = -1
        coluna = -1
        while True:
            linha = int(input('Insira a linha que deseja atirar:'))
            if validarEntrada(linha):
                break
            else:
                print("Tiro invalido entre com o valor novamente.")

        while True:
            coluna = int(input('Insira a coluna da linha para realizar o tiro:'))
            if validarEntrada(coluna):
                break
            else:
                print("Tiro invalido entre com o valor novamente")

        if linha in tiros.keys() and coluna in tiros[linha]:
            print("Tiro já realizado, tente novamente")
        else:
            if linha not in tiros.keys():
                tiros[linha] = []
            tiros[linha] = tiros[linha] + [coluna]
            break
    return (linha, coluna)

def validarTamanho(entrada, tamanho):
    return (entrada + tamanho) <= 9

def executarPosicionarBarco(navio):
    print("O barco ", navio.nome, " de tamanho ", navio.tamanho, " deve ser posicionado no campo de batalha")
    while True:
        navio.direcao = input("Entre com a direção do barco (v-Vertical, h-Horizontal): ")
        if navio.direcao in ['v', 'h']:
            break
        else:
            print('Entrada incorreta tente novamente.')
    while True:
        linha = int(input("Insira a linha para o posicionamento do barco[0 - 10]: "))
        if validarEntrada(linha) and (navio.direcao == 'h' or (navio.direcao == 'v' and validarTamanho(linha, navio.tamanho))):
            break
        else:
            print('Entrada incorreta tente novamente.')
    while True:
        coluna = int(input("Insira a coluna para o posicionamento do barco[0 - 10]: "))
        if validarEntrada(coluna) and (navio.direcao == 'v' or (navio.direcao == 'h' and validarTamanho(coluna, navio.tamanho))):
            break
        else:
            print('Entrada incorreta tente novamente.')
    return (linha, coluna, navio)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12397))

msg=s.recv(1024)
print(msg.decode('ascii'))

msg=s.recv(1024)
print(msg.decode('ascii'))

for i in range(1, 10):
    while True:
        posicao = executarPosicionarBarco(navios[i])
        b = pickle.dumps(posicao)
        s.send(b)
        respota = s.recv()
        posicaoValida = pickle.loads(respota)

        if posicaoValida:
            break

s.close()

