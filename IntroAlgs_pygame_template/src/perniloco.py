import pygame 

#cria a classe do perniloco
class Perniloco:
    def __init__(self):
        self.x = 100 #posição
        self.y = 300 #posição
        self.velocidade = 0 #subida/descida do perniloco
        self.gravidade = 0.3 #faz ele cair
        self.forca_pulo = -9 #a força quando aperta a tecla
    
    def atualizar(self): #faz cair sozinho aos poucos
        self.velocidade += self.gravidade
        self.y += self.velocidade
        if self.y > 570:
            self.y = 570
        if self.y < 0:
            self.y = 0
    
    def pular(self): #se chama, o perniloco sobe
        self.velocidade = self.forca_pulo
    
    def desenhar(self, tela): #desenha o perniloco na tela
        pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))