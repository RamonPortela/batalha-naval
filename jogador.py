class Jogador:
    
    def __init__(self, id):
        self.id = id
        self.navios = []
        self.campo = [[0] * 10] * 10
        self.tiros = []
        self.naviosAbatidos = []


    def verificarSeTiroAcertou(self, linha, coluna):
        if(self.campo[linha - 1][coluna - 1] == 1):
            return True
        else:
            return False

    def setNavioInCampo(self, linha, coluna, direcao, tamanho):
        if(direcao == 'h'):
            if(coluna + tamanho > 10):
                return False
            while tamanho > 0:
                self.campo[linha][coluna++] = 1
                tamanho--
        else:
            
            
        
