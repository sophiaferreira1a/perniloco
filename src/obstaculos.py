import pygame
import random
from src.config import LARGURA_TELA, ALTURA_TELA

class Obstaculo:
    def __init__(self, x):
        self.x = x
        self.largura = 80
        self.espaco = 250
        self.velocidade = 5
        self.passou = False

        self.imagem_original = pygame.image.load("assets/imagens/raquete.png").convert_alpha()

        self.altura_espaco = random.randint(150, ALTURA_TELA - 150 - self.espaco)
        
        self.rect_topo = pygame.Rect(self.x, 0, self.largura, self.altura_espaco)
        self.imagem_topo = pygame.transform.scale(self.imagem_original, (self.largura, self.altura_espaco))
        self.imagem_topo = pygame.transform.flip(self.imagem_topo, False, True)
        
        altura_baixo = ALTURA_TELA - (self.altura_espaco + self.espaco)
        self.rect_base = pygame.Rect(self.x, self.altura_espaco + self.espaco, self.largura, altura_baixo)
        self.imagem_base = pygame.transform.scale(self.imagem_original, (self.largura, altura_baixo))

    def atualizar(self):
        self.x -= self.velocidade
        self.rect_topo.x = self.x
        self.rect_base.x = self.x

    def desenhar(self, tela):
        tela.blit(self.imagem_topo, self.rect_topo)
        tela.blit(self.imagem_base, self.rect_base)

    def fora_da_tela(self):
        return self.x + self.largura < 0
