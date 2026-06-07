# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Perniloco 

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Francisco Filipe da Cunha Oliveira
- Nome 2: Gabriela Pinheiro Pierazolli
- Nome 3: Sophia Nicole Ferreira Reis Gonçalves
- Nome 4:

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de desviar de obstáculos

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> Na tela aparecem o Perniloco, um pernilongo em um cenário doméstico. O jogador controla as batidas de asa do mosquito pressionando a barra de espaço ou clicando na tela. O desafio é desviar de pares de raquetes elétricas mata-mosquito que surgem pelo caminho, passando pelo espaço entre elas sem se chocar. O jogo é dividido em fases com cenários diferentes, e em cada uma a velocidade, frequência e dificuldade das raquetes mudam. 

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Evitar obstáculos

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O Perniloco cai constantemente por gravidade, então sem a ação do jogador, ele desce até o chão.
- Regra 2: Cada clique, toque ou pressionamento da barra de espaço faz o Perniloco bater as asas e subir levemente.
- Regra 3: O jogador começa cada fase com 3 vidas.
- Regra 4: Colidir com uma raquete, o chão ou o teto remove 1 vida e reinicia o Perniloco na mesma fase.
- Regra 5: Perder as 3 vidas em qualquer fase reinicia o jogo completo desde a fase 1, com 3 vidas novamente.
- Regra 6: O jogador avança de fase ao atingir a pontuação exigida com pelo menos 1 vida restante.
- Regra 7: A velocidade, o espaço entre as raquetes e a frequência de aparecimento mudam a cada fase.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Completar a última fase disponível sem perder todas as vidas, se tornando o "Perniloco Imortal".

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> Perder as 3 vidas em qualquer fase.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Pernilogo, controlado pelo jogador e voa horizontalmente pela tela e responde à gravidade. Cada comando do jogador gera um impulso de subida. Ao perder uma vida, o personagem pisca brevemente antes de reaparecer na mesma fase.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Pares de raquetes elétricas mata-mosquito surgem continuamente pela direita da tela. Cada par tem uma abertura por onde o Perniloco deve passar. A posição da abertura varia a cada par. Velociade, tamanho de abertura e frequência mudam conforme a fase.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Não há itens. Ao atravessar cada par de raquetes já conta como progresso e gera pontuação. 

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa a fase com 3 vidas e 0 pontos na fase atual. A pontuação acumula 1 unidade a cada par de raquetes ultrapassado. Ao avançar de fase, as vidas são restauradas. A pontuação total da sessão é exibida na tela de fim de jogo.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Barra de espaço: mover para cima
- Clique do mouse/ toque na tela: mover para cima
- Enter: iniciar ou reiniciar a partida

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> - `main.py`: inicia o jogo e chama o loop principal;
- `src/jogo.py`: contém o loop principal e o controle de fases;
- `src/config.py`: guarda configurações como tamanho da tela, cores, velocidade e parâmetros de cada fase;
- `src/perniloco.py`: contém a classe do personagem, gravidade, movimento e controle de vidas;
- `src/obstaculos.py`: contém a classe das raquetes, geração aleatória e movimentação;
- `src/pontuacao.py`: controla a pontuação, o avanço de fase e o recorde da sessão;
- `src/telas.py`: contém as telas de início, fim de jogo e transição entre fases.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> -Imagens do personagem e das raquetes obtidas de banco de imagens gratuito;
 -Sons de zumbido, choque elétrico e efeitos de fase obtidos de banco de sons gratuito;
- Fonte personalizada estilo pixelada obtida do Google Fonts;
- A mecânica de voo com gravidade será baseada em tutoriais de Flappy Bird em Pygame, usados apenas como referência de lógica.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementar a física de gravidade e o impulso de subida do Perniloco de forma fluida;
- Dificuldade 2: Detectar colisões com precisão entre o personagem e as raquetes, especialmente nas bordas da abertura;
- Dificuldade 3: Gerenciar a transição de fases sem travar o jogo.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá o Perniloco controlado pelo teclado ou clique do mouse, raquetes elétricas surgindo e se movendo pela tela, sistema de 3 vidas por fase, pontuação crescente a cada raquete ultrapassada e tela de fim de jogo exibindo a pontuação total com opção de reiniciar.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Implementar mais de 3 fases com cenários e velocidades distintas;
- Melhoria 2: Adicionar sons como o zumbido do Perniloco, choque elétrico ao colidir e música de fundo diferente por fase.
- Melhoria 3: Adicionar animações do personagem (asas batendo, piscar ao perder vida e animação de choque ao morrer).