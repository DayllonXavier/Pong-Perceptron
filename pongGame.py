# -*- coding: utf-8 -*-
import pygame
from random import randint, uniform

from Perceptron import Perceptron
from Barra import Barra
from Bola import Bola

debug = 1 #0 -> tela jogo, 1 -> funcionamento do Perceptron

tam_tela = (640, 480)
tam_tela_debug = (1340, 640)

perceptron = Perceptron(2, 1000, "dados/dataSet", 0.001)
barra = Barra((320, 460), (80, 10), (255, 255, 255), 8, (0, tam_tela[0]))
bola = Bola((255, 255, 255), 13, 6, (3, 9), (0, tam_tela[0]), (0, tam_tela[1]))

pygame.init()
pygame.display.set_caption("PONG AI")

if (debug):
    tela = pygame.display.set_mode(tam_tela_debug, 0, 32)
    separacao_x = 60
else:
    tela = pygame.display.set_mode(tam_tela, 0, 32)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

FPS = 30
pontuacao = 0
colisao = False
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                FPS = max(10, FPS - 10)
            elif (event.key == pygame.K_RIGHT):
                FPS = min(500, FPS + 10)
            print("FPS: {}".format(FPS))

    if (bola.alcancou_base_y()):
        pontuacao = 0
        bola.iniciar_valores()
        print("Treinando Perceptron")
        perceptron.treinar_epoca()

    if (bola.pos[1] > 0):
        acao = perceptron.forward([barra.pos[0], bola.pos[0]])
        barra.movimentar(acao)

    if ((bola.pos[0] > barra.pos[0] - bola.raio - barra.tam[0] / 2.0 and bola.pos[0] < barra.pos[0] + bola.raio + barra.tam[0]/2.0) and
        (bola.pos[1] > barra.pos[1] - bola.raio / 2.0 - barra.tam[1] / 2.0 and bola.pos[1] < barra.pos[1] + barra.tam[1]/2.0)):
        if (not colisao):
            pontuacao += 1
            if (pontuacao % 5 == 0):
                bola.aleatorizar_velocidade_y()
            bola.inverter_velocidade_y()
        colisao = True
    else:
        colisao = False

    tela.fill((0,0,0))
    clock.tick(FPS)

    epocasText = font.render("Épocas: " + str(perceptron.epocas), 1, (255,255,255))
    tela.blit(epocasText, (30, 20))

    pontosText = font.render("Pontos: " + str(pontuacao), 1, (255, 255, 255))
    tela.blit(pontosText, (tam_tela[0] - pontosText.get_width() - 30, 20))

    bola.renderizar(tela)
    bola.movimentar()

    barra.renderizar(tela)

    if (debug):
        pygame.draw.rect(tela, (120, 120, 120), pygame.Rect((tam_tela[0], 0), (separacao_x, tam_tela_debug[1])))
        pygame.draw.rect(tela, (120, 120, 120), pygame.Rect((0, tam_tela[1]), (tam_tela[0], tam_tela_debug[1] - tam_tela[1])))

        pontos_x = [0, 650]
        pontos = []
        for x in pontos_x:
            pontos.append((tam_tela[0] + separacao_x + x, tam_tela_debug[1] - int((perceptron.pesos_sinapticos[0] - (x * perceptron.pesos_sinapticos[1])) / perceptron.pesos_sinapticos[2])))

        pygame.draw.lines(tela, (251, 113, 25), False, pontos, 5)

        for amostra in perceptron.dataSet:
            if (amostra[2][0] == 1):
                cor = (0, 0, 255)
            else:
                cor = (255, 0, 0)
            pygame.draw.circle(tela, cor, (tam_tela[0] + separacao_x + int(amostra[1][0]), tam_tela_debug[1] - int(amostra[1][1])), 5)

        pygame.draw.circle(tela, (0, 255, 0), (tam_tela[0] + separacao_x + int(barra.pos[0]), tam_tela_debug[1] - int(bola.pos[0])), 7)

    pygame.display.update()
