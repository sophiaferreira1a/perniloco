from src.pontuacao import carregar_ranking, adicionar_ao_ranking

CAMINHO_TESTE_RANKING = "data/test_ranking.txt"

def test_adicionar_ao_ranking():
    with open(CAMINHO_TESTE_RANKING, "w") as f:
        f.write("")
        
    ranking = adicionar_ao_ranking(10, CAMINHO_TESTE_RANKING)
    assert ranking == [10]
    
    adicionar_ao_ranking(20, CAMINHO_TESTE_RANKING)
    adicionar_ao_ranking(30, CAMINHO_TESTE_RANKING)
    adicionar_ao_ranking(40, CAMINHO_TESTE_RANKING)
    ranking = adicionar_ao_ranking(50, CAMINHO_TESTE_RANKING)
    assert ranking == [50, 40, 30, 20, 10]
    
    ranking = adicionar_ao_ranking(60, CAMINHO_TESTE_RANKING)
    assert ranking == [60, 50, 40, 30, 20]
    assert len(ranking) == 5

if __name__ == "__main__":
    test_adicionar_ao_ranking()
    print("Teste de ranking passou!")
