import pygame 

#cria a classe do perniloco
class Perniloco:
    def __init__(self, carregar_sprite=True):
        self.x = 100
        self.y = 300
        self.velocidade = 0
        self.gravidade = 0.3
        self.forca_pulo = -9

        if carregar_sprite:
            self.sprite = pygame.image.load("assets/imagens/perniloco-1.png").convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.rect = self.sprite.get_rect(center=(self.x, self.y))
        else:
            self.sprite = None
            self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def atualizar(self): #faz cair sozinho aos poucos
        self.velocidade += self.gravidade
        self.y += self.velocidade
        if self.y > 570:
            self.y = 570
        if self.y < 0:
            self.y = 0
        self.rect.center = (self.x, self.y)
    def pular(self): #se chama, o perniloco sobe
        self.velocidade = self.forca_pulo
    
    def desenhar(self, tela): #desenha o perniloco na tela (rotaciona para cima se estiver movendo pra cima e vice-versa)
        if self.sprite is None:
            return
        self.angulo = -self.velocidade * 3 #ângulo de inclinação
        if self.angulo > 25:
            self.angulo = 25
        if self.angulo < -90:
            self.angulo = -90
        sprite_rotacionado = pygame.transform.rotate(self.sprite, self.angulo)
        novo_rect = sprite_rotacionado.get_rect(center=self.rect.center)

        tela.blit(sprite_rotacionado, novo_rect)
