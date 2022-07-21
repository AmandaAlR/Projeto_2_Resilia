'''
4 perguntas
Para iniciar o questionário será solicitado ao usuário que informe a sua idade e
gênero. Cada linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1,
resposta_2, resposta_3, resposta_4, data e hora da resposta
'''
from datetime import datetime
import pandas as pd
import csv
import os
import time

idade = input("\nOlá, bem vindo a nossa pesquisa eleitoral. Por favor, escreva a sua idade:\nOBS: Para sair da pesquisa, escreva 00.\n")
genero = 
cidade = 
pergunta1 = 
pergunta2 = 
pergunta3 = 
porgunta4 = 
pergunta5 = 

class Eleitor(): # Carol
    def __init__(self, idade, genero, cidade):
        self.idade = idade
        self.genero = genero
        self.cidade = cidade

class Pesquisa(): # Aline
    def __init__(self, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5):
        self.pergunta1 = pergunta1
        self.pergunta2 = pergunta2
        self.pergunta3 = pergunta3
        self.pergunta4 = pergunta4
        self.pergunta5 = pergunta5

class Hora(): # Carlos
    def __init__(self, hora):
        self.hora = Hora(datetime.now)

class Registrar_dados: # Karol, Amanda (Pesquisar Pandas) e Carlos
    def __init__(self, planilha):
        self.planilha = dict(planilha)

    def conectar_planilha:

    def salvar_dados:

    def atualizar_dados:

class Atualizar_dados: # Karol e Carlos
    def

eleitor = Eleitor()