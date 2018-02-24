import socket

# Cria o socket
tiros = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 12397))

msg=s.recv(1024)
print(msg.decode('ascii'))

def validarEntrada(entrada):
    if entrada < 0 and entrada > 9:
        return True
    else:
        return False

def atirar():
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
    return (entrada + tamanho) < 9

def posicionarBarco(nome, tamanho):
    print("O barco ", nome, " de tamanho ", tamanho, " deve ser posicionado no campo de batalha")
    while True:
        direcao = input("Entre com a direção do barco (v-Vertical, h-Horizontal")
        if direcao in ['v', 'h']:
            break
        else:
            print('Entrada incorreta tente novamente.')
    while True:
        linha = input("Insira a linha para o posicionamento do barco:")
        if validarEntrada(linha) and (direcao == 'h' or (direcao == 'v' and validarTamanho(linha, tamanho))):
            break
        else:
            print('Entrada incorreta tente novamente.')
    while True:
        coluna = input("Insira a coluna para o posicionamento do barco:")
        if validarEntrada(coluna) and (direcao == 'v' or (direcao == 'h' and validarTamanho(coluna, tamanho))):
            break
        else:
            print('Entrada incorreta tente novamente.')
    return (linha, coluna, direcao)