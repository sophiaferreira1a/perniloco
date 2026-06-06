import sys
import os
import pygame

pygame.init()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.perniloco import Perniloco


def test_pular():
    p = Perniloco(carregar_sprite=False)
    
    p.pular()
    
    assert p.velocidade == p.forca_pulo


def test_gravidade():
    p = Perniloco(carregar_sprite=False)
    
    velocidade_inicial = p.velocidade
    
    p.atualizar()
    
    assert p.velocidade > velocidade_inicial


def test_limite_chao():
    p = Perniloco(carregar_sprite=False)
    
    p.y = 1000
    p.atualizar()
    
    assert p.y <= 570
