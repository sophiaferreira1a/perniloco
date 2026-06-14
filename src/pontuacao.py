def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

def carregar_recorde(caminho):
    """Carrega o recorde do arquivo. Se não existir ou for inválido, retorna 0."""
    try:
        with open(caminho, "r") as f:
            conteudo = f.read().strip()
            return int(conteudo) if conteudo else 0
    except (FileNotFoundError, ValueError, IOError):
        return 0

def salvar_recorde(caminho, recorde):
    """Salva o recorde no arquivo."""
    try:
        with open(caminho, "w") as f:
            f.write(str(recorde))
    except IOError as e:
        print(f"Erro ao salvar recorde: {e}")

def atualizar_recorde(pontos_atuais, recorde_atual, caminho):
    """Verifica se houve novo recorde e salva se necessário."""
    if pontos_atuais > recorde_atual:
        salvar_recorde(caminho, pontos_atuais)
        return pontos_atuais
    return recorde_atual

def carregar_ranking(caminho):
    """Carrega o histórico das últimas 5 pontuações."""
    try:
        with open(caminho, "r") as f:
            return [int(linha.strip()) for linha in f.readlines() if linha.strip()]
    except (FileNotFoundError, ValueError, IOError):
        return []

def salvar_ranking(caminho, ranking):
    """Salva o ranking no arquivo."""
    try:
        with open(caminho, "w") as f:
            for ponto in ranking:
                f.write(f"{ponto}\n")
    except IOError as e:
        print(f"Erro ao salvar ranking: {e}")

def adicionar_ao_ranking(pontos, caminho):
    """Adiciona uma nova pontuação ao histórico (mantém as últimas 5)."""
    ranking = carregar_ranking(caminho)
    ranking.insert(0, pontos)
    ranking = ranking[:5]
    salvar_ranking(caminho, ranking)
    return ranking