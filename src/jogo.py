import pygame
from perniloco import Perniloco

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def rodar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    imagem_fundo = pygame.image.load("assets/imagens/quarto.png").convert()
    background = pygame.transform.scale(imagem_fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Perniloco")
    mosquito = Perniloco()
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    mosquito.pular()
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
        mosquito.atualizar()
        tela.blit(background, (0, 0))  
        mosquito.desenhar(tela)
        pygame.display.update()
        clock.tick(60)
        print(mosquito.y)

    pygame.quit()

if __name__ == "__main__":
    rodar_jogo()