from datetime import datetime
import pandas as pd
from os import path
import time as t


class Sistema():
    lista_eleitores = []
    def __init__(self):
        self.eleitor() # apresenta o menu principal
        self.salvar() # salva aqui cada eleitor
    
    def eleitor(self): # registro dos eleitores em loop 10x
        loop = True
        while loop:
            eleitor = Eleitor()
            eleitor.cadastrar_eleitor()
            if eleitor.idade == '00':
                print('\nPesquisa encerrada, agradecemos sua atenção.\n')
                loop = False
            else:
                self.lista_eleitores.append(eleitor)


    def salvar(self): # salvar os eleitores no csv
        controle_csv = Registrar_dados()
        eleitores_dict = []
        for eleitor in self.lista_eleitores:
            eleitores_dict.append(eleitor.exportar_eleitor())
        controle_csv.criar_csv(eleitores_dict)

class Eleitor(): # Carol
    def __init__(self):
        self.hora = datetime.now()

    def cadastrar_eleitor(self):
        self.get_idade()
        if self.idade == '00':
            return self
        self.get_genero()
        self.get_pergunta1()
        self.get_pergunta2()
        self.get_pergunta3()
        self.get_pergunta4()
        self.get_pergunta5()

    def get_idade(self):
        loop = True
        while loop:
            idade = input("\nOlá, bem vindo(a) a nossa pesquisa eleitoral.\nAntes de começarmos gostaria de informar que essa pesquisa será utilizada apenas para fins educativos, sem nenhum cunho político.\n\nSerão feitas 5 perguntas de múltipla escolha e caso você queira encerrar a pesquisa, digite 00 na área da idade.\n\nPor favor, escreva a sua idade:\n")
            t.sleep(2)
            if idade == '00':
                self.idade = idade
                return
            elif int(idade) >= 16 and int(idade) < 100:
                self.idade = idade
                return
            elif int(idade) >= 1 and int(idade) <=15:
                print(f'\nDe acordo com a Constituição Federal, em outubro de 1988, foi estabelecido o voto facultativo para os jovens maiores de 16 e menores de 18 anos, em seu art. 14, § 1º, inciso II, alínea c. Então você precisa ter idade acima de 16 anos para votar.Agradecemos sua compreensão.\n')
                t.sleep(2)
            else:
                print(f'\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def get_genero(self):
        loop = True
        while loop:
            genero = input("\nQual o seu gênero?\n[1] - Feminino\n[2] - Masculino\n[3] - Não-binário \n[4] - Prefiro não responder\n")
            t.sleep(2)
            if genero == '1':
                self.genero = genero
                loop = False
            elif genero == '2':
                self.genero = genero
                loop = False
            elif genero == '3':
                self.genero = genero
                loop = False
            elif genero == '4':
                self.genero = genero
                loop = False
            else:
                print(f'\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')
                  
    def get_pergunta1(self):
        loop = True
        while loop:
            pergunta1 = input("\n1. O ato de votar é importante para você?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            t.sleep(2)
            if pergunta1 == '1':
                self.pergunta1 = pergunta1
                loop = False
            elif pergunta1 == '2':
                self.pergunta1 = pergunta1
                loop = False
            elif pergunta1 == '3':
                self.pergunta1 = pergunta1
                loop = False
            else:
                print('\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def get_pergunta2(self):
        loop = True
        while loop:
            pergunta2 = input("\n2. Você sabe a diferença entre o voto branco e nulo?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            t.sleep(2)
            if pergunta2 == '1':
                self.pergunta2 = pergunta2
                loop = False
            elif pergunta2 == '2':
                self.pergunta2 = pergunta2
                loop = False
            elif pergunta2 == '3':
                self.pergunta2 = pergunta2
                loop = False
            else:
                print('\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def get_pergunta3(self):
        loop = True
        while loop:
            pergunta3 = input("\n3. Você é a favor do voto obrigatório?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            t.sleep(2)
            if pergunta3 == '1':
                self.pergunta3 = pergunta3
                loop = False
            elif pergunta3 == '2':
                self.pergunta3 = pergunta3
                loop = False
            elif pergunta3 == '3':
                self.pergunta3 = pergunta3
                loop = False
            else:
                print('\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def get_pergunta4(self):
        loop = True
        while loop:
            pergunta4 = input("\n4. Você já tem a biometria cadastrada?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            t.sleep(2)
            if pergunta4 == '1':
                self.pergunta4 = pergunta4
                loop = False
            elif pergunta4 == '2':
                self.pergunta4 = pergunta4
                loop = False
            elif pergunta4 == '3':
                self.pergunta4 = pergunta4
                loop = False
            else:
                print('\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def get_pergunta5(self):
        loop = True
        while loop:
            pergunta5 = input("\n5. Você acredita que a urna eletrônica é confiável?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            t.sleep(2)
            if pergunta5 == '1':
                self.pergunta5 = pergunta5
                print('\nRespostas registradas.Muito obrigado por sua colaboração!\n')
                loop = False
            elif pergunta5 == '2':
                self.pergunta5 = pergunta5
                print('\nRespostas registradas.Muito obrigado por sua colaboração!\n')
                loop = False
            elif pergunta5 == '3':
                self.pergunta5 = pergunta5
                print(f'\nRespostas registradas. Muito obrigado por sua colaboração!\n')
                loop = False
            else:
                print('\nPor gentileza, digite a opção desejada de acordo com o menu apresentado!\n')

    def exportar_eleitor(self):
        return self.__dict__

class Registrar_dados():
    columns = ["data_hora", "idade", "genero", "pergunta1", "pergunta2", "pergunta3", "pergunta4", "pergunta5"]
    def __init__(self):
        if not path.exists("pesquisa_eleitoral.csv"):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(r'pesquisa_eleitoral.csv', index = False, header=True)
    def criar_csv(self, lista_eleitores):
        df = pd.DataFrame.from_dict(lista_eleitores) 
        df.to_csv(r'pesquisa_eleitoral.csv', index = False, header=False, mode='a')



sistema = Sistema()