import pygame
from src.perniloco import Perniloco 

def rodar_jogo():
    pygame.init()
    #define as configurações iniciais
    tela = pygame.display.set_mode( (800, 600)) #tamanho da tela a ser mostrado
    pygame.display.set_caption("Perniloco") #exibe o título
    mosquito = Perniloco()
    clock = pygame.time.Clock()
    rodando = True

    while rodando: #loop do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #o jogo sai se a condição se torna falsa
                rodando = False
            if evento.type == pygame.KEYDOWN: #se alguma tecla for pressionada
                if evento.key == pygame.K_SPACE:
                    mosquito.pular() # se aperta o espaço, o mosquito pula
        mosquito.atualizar()
        tela.fill((0, 0, 0))
        mosquito.desenhar(tela)
        pygame.display.update()
        clock.tick(60) #faz o programa rodar a 60fps
        print(mosquito.y)

    pygame.quit()
