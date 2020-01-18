# -*- coding: utf-8 -*-
from random import randint

def carregar_dados(endereco, qtd_entradas, qtd_saidas):
    """
        Retorna uma tupla com 3 valores:
            - indice da amostra;
            - lista com os valores de entrada (na ordem);
            - lista com os valores da saída (na ordem).
    """

    debug = 0
    if debug:
        print("Iniciando Leitura dos Dados")
    datas = [];
    with open(endereco, 'r') as arq:
        lines = arq.readlines()
        for line in lines:
            line = list(map(float, line.strip().split(" ")))
            data = (line[0], [], [])

            for i in range(0, qtd_entradas):
                data[1].append(line[i+1])

            for i in range(0, qtd_saidas):
                data[2].append(line[i+1+qtd_entradas])

            datas.append(data)
            if debug:
                print(data)
    if debug:
        print("Finalizando Leitura dos Dados")
    return datas
