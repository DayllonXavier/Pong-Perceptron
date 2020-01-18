# -*- coding: utf-8 -*-
from random import uniform

def gerar_dados(endereco):
    """
        Gera os dados e salva no aquivo no formato:
        '<ID da amostra> <entradas da rede> <saídas da rede>'
    """
    qtd_amostras = 500
    with open(endereco, "w") as arq:
        for i in range(0, qtd_amostras):
            salv = str(i+1)
            x1 = uniform(0, 640)
            x2 = uniform(0, 640)
            if (x1 > x2):
                resp = "-1.0"
            else:
                resp = "1.0"
            salv += " " + str(x1) + " " + str(x2) + " " + resp + "\n"
            arq.write(salv)

gerar_dados("dataSet")
