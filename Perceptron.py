# -*- coding: utf-8 -*-
from random import random

from funcoes import carregar_dados

class Perceptron(object):
    def __init__(self, qtd_entradas, max_epocas, dataSet_endereco, learning_rate):
        self.qtd_entradas = qtd_entradas
        self.learning_rate = learning_rate
        self.pesos_sinapticos = [random()] #valor do limiar de ativação na posição 0 da lista
        self.dataSet = []
        self.epocas = 0
        self.definir_max_epocas(max_epocas)
        self.definir_endereco_dataSet(dataSet_endereco)
        self.iniciar_pesos(qtd_entradas)
        self.carregar_dataSet()

    def definir_max_epocas(self, max_epocas):
        self.max_epocas = max_epocas

    def definir_endereco_dataSet(self, dataSet_endereco):
        self.dataSet_endereco = dataSet_endereco

    def iniciar_pesos(self, qtd_entradas):
        for i in range(0, qtd_entradas):
            self.pesos_sinapticos.append(random()) #Pesos iniciados no intervalo [0, 1)

    def carregar_dataSet(self):
        self.dataSet = carregar_dados(self.dataSet_endereco, self.qtd_entradas, 1)

    def ajustar_dados(self, dados):
        dados = [-1.0] + dados
        return dados

    def copia_lista(self, lista):
        nova = []
        for item in lista:
            nova.append(item)
        return nova

    def degrau_bipolar(self, num): #Função de ativação
        if (num >= 0):
            return 1.0
        else:
            return -1.0

    def forward(self, entradas):
        entradas = self.ajustar_dados(entradas)
        saida = 0.0
        for i in range(0, self.qtd_entradas+1):
            saida += (entradas[i] * self.pesos_sinapticos[i])
        return self.degrau_bipolar(saida)

    def treinar_epoca(self):
        for amostra in self.dataSet:
            entradas = self.copia_lista(amostra[1])
            resp = self.forward(entradas)
            if (resp != amostra[2][0]):
                entradas = self.ajustar_dados(entradas)

                for i in range(0, self.qtd_entradas+1):
                    self.pesos_sinapticos[i] = self.pesos_sinapticos[i] + self.learning_rate * (amostra[2][0] - resp) * entradas[i]

        self.epocas += 1

    def treinar_rede(self):
        print("Iniciando Treinamento")
        erro = 1
        while (erro):
            erro = 0
            for amostra in self.dataSet:
                resp = self.forward(self.copia_lista(amostra[1]))
                if (resp != amostra[2][0]):
                    erro = 1
                    break

            if (erro):
                if (self.epocas == self.max_epocas):
                    print("Limite de epocas alcandados {}".format(self.epocas))
                    print("Status: Rede não treinada")
                    break
                self.treinar_epoca()
        print("Finalizando Treinamento! {} epocas".format(self.epocas))
