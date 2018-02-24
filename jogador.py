class Jogador:
    
    def __init__(self, id):
        self.id = id
        self.navios = []
        self.campo = [[0] * 10] * 10
        self.tiros = []
        self.naviosAbatidos = []


    def verificarSeTiroAcertou(self, linha, coluna):
        if(self.campo[linha][coluna] == 1):
            return True
        else:
            return False

    def setNavioInCampo(self, linha, coluna, direcao, tamanho):
        if(direcao == 'h'):
            if(coluna + tamanho > 10):
                return False
            while tamanho > 0:
                self.campo[linha][coluna] = 1
                tamanho = tamanho - 1
                coluna = coluna + 1
        else:
            if(linha + tamanho > 10):
                return False
            while tamanho > 0:
                self.campo[linha][coluna] = 1
                linha = linha + 1
                tamanho = tamanho - 1
        return True

    def atirar(self):
        linha = -1
        while True:
            linha = input('Insira a linha que deseja atirar')
            if linha < 0 and linha > 9:
                break