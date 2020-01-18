# Pong-Perceptron

  Este projeto tem fins de aprendizagem, sendo tal aplicação de uma rede neural Perceptron para jogar uma versão reduzida do clássico jogo "Pong".
  
  A rede neural possuí um conjunto de dados, os quais são os dados de treinamentos exposto ao Perceptron toda vez que ele perde o jogo!
  
  O Perceptron tem duas entradas:
  - Posição x da barra;
  - Posição x da bola.
  
  O Perceptron procura manter essas posições sempre iguais, isto é, faz a barra (controlada pelo Perceptron) tentar sempre ter a mesma posição no eixo-x da Bola, ou seja, o Perceptron tenta encontrar a reta que separa os movimentos de onde a "barra" deve se deslocar para direita e para esquerda, tal reta, por serem as entradas de mesma dimensão, é necessáriamente a reta bissetriz entre o eixo da posição x da barra com o eixo da posição x da bola.
  
  O Perceptron tem duas saídas possíveis:
  - 1 -> movimento para direita;
  - -1 -> movimento para a esquerda.
    
  Caso a variável "debug" do arquivo "pongGame.py" estiver definida com o valor 0, será mostrado apenas a tela de jogo, porém caso esteja definida com qualquer outro valor, será então exibido a forma que a rede neural está atuando!

  ### Requerimentos:
    - Python 3
    - PyGame
    
  Para executar use:
        python pongGame.py
  
    
