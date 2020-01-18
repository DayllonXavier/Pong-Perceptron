# -*- coding: utf-8 -*-
from pygame.draw import circle
from random import randint

class Bola(object):
    def __init__(self, cor, raio, velocidade_x, intervalo_velocidade_y, intervalo_pos_x, intervalo_pos_y):
        self.definir_cor(cor)
        self.definir_raio(raio)
        self.definir_velocidade_x(velocidade_x)
        self.definir_intervalo_velocidade_y(intervalo_velocidade_y)
        self.definir_intervalo_pos_x(intervalo_pos_x)
        self.definir_intervalo_pos_y(intervalo_pos_y)
        self.iniciar_valores()

    def definir_cor(self, cor):
        self.cor = cor

    def definir_pos(self, pos):
        self.pos = pos

    def definir_raio(self, raio):
        self.raio = raio

    def definir_velocidade_x(self, velocidade_x):
        self.velocidade_x = velocidade_x

    def definir_intervalo_velocidade_y(self, intervalo_velocidade_y):
        self.intervalo_velocidade_y = intervalo_velocidade_y

    def definir_intervalo_pos_x(self, intervalo_pos_x):
        self.intervalo_pos_x = intervalo_pos_x

    def definir_intervalo_pos_y(self, intervalo_pos_y):
        self.intervalo_pos_y = intervalo_pos_y

    def aleatorizar_velocidade_y(self):
        self.velocidade_y = randint(self.intervalo_velocidade_y[0], self.intervalo_velocidade_y[1])

    def inverter_velocidade_x(self):
        self.velocidade_x *= -1

    def inverter_velocidade_y(self):
        self.velocidade_y *= -1

    def iniciar_valores(self):
        self.aleatorizar_velocidade_y()
        self.definir_pos((randint(self.intervalo_pos_x[0] + self.raio, self.intervalo_pos_x[1] - self.raio), -1 * self.raio))

    def alcancou_limite_x(self):
        if (self.pos[0] - self.raio <= self.intervalo_pos_x[0]):
            return 1
        if (self.pos[0] + self.raio >= self.intervalo_pos_x[1]):
            return 1
        return 0

    def alcancou_base_y(self):
        if (self.pos[1] >= self.intervalo_pos_y[1] + self.raio):
            return 1
        return 0

    def alcancou_topo_y(self):
        if (self.pos[1] <= self.intervalo_pos_y[0]):
            return 1
        return 0

    def movimentar(self):
        if (self.alcancou_topo_y() and self.velocidade_y < 0):
            self.inverter_velocidade_y()
        if (self.alcancou_limite_x()):
            self.inverter_velocidade_x()
        self.definir_pos((self.pos[0] + self.velocidade_x, self.pos[1] + self.velocidade_y))

    def renderizar(self, tela):
        circle(tela, self.cor, self.pos, self.raio, 0)
