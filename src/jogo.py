import pygame
from src.perniloco import Perniloco
from src.obstaculos import Obstaculo
from src.config import LARGURA_TELA, ALTURA_TELA, FPS, BRANCO, TROCA_FASE, FIM_JOGO, CAMINHO_RECORDE, CAMINHO_RANKING
from src.pontuacao import carregar_recorde, atualizar_recorde, carregar_ranking, adicionar_ao_ranking

def rodar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    
    fundo_quarto = pygame.image.load("assets/imagens/quarto.png").convert()
    fundo_quarto = pygame.transform.scale(fundo_quarto, (LARGURA_TELA, ALTURA_TELA))
    fundo_cozinha = pygame.image.load("assets/imagens/cozinha.png").convert()
    fundo_cozinha = pygame.transform.scale(fundo_cozinha, (LARGURA_TELA, ALTURA_TELA))
    
    background = fundo_quarto
    
    imagem_coracao = pygame.image.load("assets/imagens/coracao.png").convert_alpha()
    imagem_coracao = pygame.transform.scale(imagem_coracao, (30, 30))
    vidas = 3
    tempo_invulneravel = 0
    
    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)
    
    fonte = pygame.font.SysFont("Arial", 32, bold=True)
    fonte_recorde = pygame.font.SysFont("Arial", 24, bold=True)
    fonte_vitoria = pygame.font.SysFont("Arial", 48, bold=True)
    
    pygame.display.set_caption("Perniloco")
    
    mosquito = Perniloco()
    obstaculos = [Obstaculo(LARGURA_TELA + 200)]
    
    clock = pygame.time.Clock()
    rodando = True
    venceu = False
    perdeu = False
    ranking_atualizado = False

    while rodando:
        dt = clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if (venceu or perdeu) and (evento.key in [pygame.K_SPACE, pygame.K_UP, pygame.K_r]):
                    vidas = 3
                    tempo_invulneravel = 0
                    pontos = 0
                    recorde = carregar_recorde(CAMINHO_RECORDE)
                    ranking = carregar_ranking(CAMINHO_RANKING)
                    background = fundo_quarto
                    mosquito = Perniloco()
                    obstaculos = [Obstaculo(LARGURA_TELA + 200)]
                    venceu = False
                    perdeu = False
                    ranking_atualizado = False
                elif evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    mosquito.pular()
                elif evento.key == pygame.K_ESCAPE:
                    rodando = False
        
        if not venceu and not perdeu:
            mosquito.atualizar()
            
            if tempo_invulneravel > 0:
                tempo_invulneravel -= dt

            for obs in obstaculos:
                obs.atualizar()
                
                if not obs.passou and obs.x + obs.largura < mosquito.x:
                    pontos += 1
                    obs.passou = True
                    
                    recorde = atualizar_recorde(pontos, recorde, CAMINHO_RECORDE)
                    
                    if pontos == TROCA_FASE:
                        background = fundo_cozinha
                    
                    if pontos >= FIM_JOGO:
                        venceu = True

                if tempo_invulneravel <= 0:
                    if mosquito.rect.colliderect(obs.rect_topo) or mosquito.rect.colliderect(obs.rect_base):
                        vidas -= 1
                        tempo_invulneravel = 1500
                        if vidas <= 0:
                            perdeu = True
                
            if obstaculos[-1].x < LARGURA_TELA - 300:
                obstaculos.append(Obstaculo(LARGURA_TELA))
                
            if obstaculos[0].fora_da_tela():
                obstaculos.pop(0)

        tela.blit(background, (0, 0))  
        for obs in obstaculos:
            obs.desenhar(tela)
        
        if not venceu and not perdeu:
            if tempo_invulneravel <= 0 or (pygame.time.get_ticks() // 100) % 2 == 0:
                mosquito.desenhar(tela)
        
        for i in range(vidas):
            tela.blit(imagem_coracao, (10 + i * 35, 10))
            
        texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (LARGURA_TELA - texto_pontos.get_width() - 20, 10))
        
        texto_recorde = fonte_recorde.render(f"Recorde: {recorde}", True, BRANCO)
        tela.blit(texto_recorde, (LARGURA_TELA - texto_recorde.get_width() - 20, 50))
        
        if venceu or perdeu:
            if not ranking_atualizado:
                ranking = adicionar_ao_ranking(pontos, CAMINHO_RANKING)
                ranking_atualizado = True

            overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            tela.blit(overlay, (0, 0))
            
            texto_principal = "Fim do jogo. Você venceu!" if venceu else "Fim de jogo. Você perdeu :("
            msg_final = fonte_vitoria.render(texto_principal, True, BRANCO)
            msg_score = fonte.render(f"Pontuação Final: {pontos}", True, BRANCO)
            msg_recorde_final = fonte.render(f"Melhor Pontuação: {recorde}", True, BRANCO)
            msg_reiniciar = fonte.render("Pressione ESPAÇO ou R para Reiniciar", True, BRANCO)
            msg_sair = fonte.render("Pressione ESC para Sair", True, BRANCO)
            
            tela.blit(msg_final, (LARGURA_TELA//2 - msg_final.get_width()//2, ALTURA_TELA//2 - 180))
            tela.blit(msg_score, (LARGURA_TELA//2 - msg_score.get_width()//2, ALTURA_TELA//2 - 110))
            tela.blit(msg_recorde_final, (LARGURA_TELA//2 - msg_recorde_final.get_width()//2, ALTURA_TELA//2 - 60))
            
            texto_hist_titulo = fonte_recorde.render("Histórico (Últimos 5 jogos):", True, BRANCO)
            tela.blit(texto_hist_titulo, (LARGURA_TELA//2 - texto_hist_titulo.get_width()//2, ALTURA_TELA//2 - 10))
            
            for i, p in enumerate(ranking):
                texto_item = fonte_recorde.render(f"{i+1}º: {p} pontos", True, BRANCO)
                tela.blit(texto_item, (LARGURA_TELA//2 - texto_item.get_width()//2, ALTURA_TELA//2 + 20 + i * 25))

            tela.blit(msg_reiniciar, (LARGURA_TELA//2 - msg_reiniciar.get_width()//2, ALTURA_TELA//2 + 160))
            tela.blit(msg_sair, (LARGURA_TELA//2 - msg_sair.get_width()//2, ALTURA_TELA//2 + 210))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    rodar_jogo()
