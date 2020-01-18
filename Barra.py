# -*- coding: utf-8 -*-
from pygame.draw import rect
from pygame import Rect

class Barra(object):
    def __init__(self, pos, tam, cor, velocidade, intervalo_pos_x):
        self.definir_velocidade(velocidade)
        self.definir_posicao(pos)
        self.definir_tamanho(tam)
        self.definir_cor(cor)
        self.definir_intervalo_pos_x(intervalo_pos_x);

    def definir_velocidade(self, velocidade):
        self.velocidade = velocidade

    def definir_posicao(self, pos):
        self.pos = pos

    def definir_tamanho(self, tam):
        self.tam = tam

    def definir_cor(self, cor):
        self.cor = cor

    def definir_intervalo_pos_x(self, intervalo_pos_x):
        self.intervalo_pos_x = intervalo_pos_x

    def ajustar_posicao(self):
        return (self.pos[0] - self.tam[0] / 2.0, self.pos[1] - self.tam[1] / 2.0)

    def renderizar(self, tela):
        rect(tela, self.cor, Rect(self.ajustar_posicao(), self.tam))

    def movimentar(self, fator):
        self.definir_posicao((max(self.intervalo_pos_x[0], min(self.intervalo_pos_x[1], self.pos[0] + (self.velocidade * fator))), self.pos[1]))
