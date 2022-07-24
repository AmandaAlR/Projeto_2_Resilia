from datetime import datetime
import pandas as pd
import csv
from os import path

class Sistema():
    lista_eleitores = []
    def __init__(self):
        self.apresentacao() # apresenta o menu principal
        self.salvar() # salva aqui cada eleitor

    def apresentacao(self):
        loop = True
        while loop:
            apresentacao = input("Olá, bem vindo(a) a nossa pesquisa eleitoral.\nAntes de começarmos gostaria de informar que essa pesquisa será utilizada apenas para fins educativos, sem nenhum cunho político.\nSerão feitas 5 perguntas de múltipla escolha e caso você queira encerrar a pesquisa, digite 00 na área da idade.\nVocê gostaria de participar dessa pesquisa sim ou não?\n[1] - Sim\n[2] - Não e sair\n")
            if apresentacao == '1':
                self.eleitor()
                loop = False
            else:
                exit()

    
    def eleitor(self): # registro dos eleitores em loop 10x
        loop = True
        while loop:
            eleitor = Eleitor()
            eleitor.cadastrar_eleitor()
            if eleitor.idade == '00':
                print('Pesquisa encerrada, agradecemos sua atenção.')
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
        self.get_cidade()
        self.get_pergunta1()
        self.get_pergunta2()
        self.get_pergunta3()
        self.get_pergunta4()
        self.get_pergunta5()

    def get_idade(self):
        loop = True
        while loop:
            idade = input("\nPor favor, escreva a sua idade:\nOBS: Para sair da pesquisa, escreva 00.\n")
            if idade == '00':
                self.idade = idade
                return
            elif int(idade) >= 16 and int(idade) < 100:
                self.idade = idade
                return
            elif int(idade) >= 1 and int(idade) <=15:
                print(f'Muito obrigado pelo seu interesse em responder nossa pesquisa! Porém, nosso objetivo é entender melhor como pensam os brasileiros(as) que podem ser eleitores(as) na presente data, isto é, todos aqueles(as) a partir de 16 anos de idade. Agradecemos sua compreensão.')
            else:
                print(f'Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!')

    def get_genero(self):
        loop = True
        while loop:
            genero = input("Qual o seu gênero?\n[1] - Feminino\n[2] - Masculino\n[3] - Transgênero \n[4] - Não-binário \n[5]- Prefiro não responder\n")
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
            elif genero == '5':
                self.genero = genero
                loop = False
            else:
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def get_cidade(self):
        loop = True
        while loop:
            cidade = input("Qual a cidade onde você mora?\n[1] - Belo Horizonte(MG) \n[2] - Contagem(MG) \n[3] - Recife(PE) \n[4] - São Paulo(SP) \n[5] - Três Barras(SC) \n[6] - Outra\n")
            if cidade =='1':
                self.cidade = cidade
                loop = False
            elif cidade =='2':
                self.cidade = cidade
                loop = False
            elif cidade =='3':
                self.cidade = cidade
                loop = False
            elif cidade =='4':
                self.cidade = cidade
                loop = False
            elif cidade =='5':
                self.cidade = cidade
                loop = False
            elif cidade =='6':
                self.cidade = cidade
                loop = False
            else:
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")
                  
    def get_pergunta1(self):
        loop = True
        while loop:
            pergunta1 = input("1. O ato de votar é importante para você?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
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
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def get_pergunta2(self):
        loop = True
        while loop:
            pergunta2 = input("2. Você sabe a diferença entre o voto branco e nulo?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
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
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def get_pergunta3(self):
        loop = True
        while loop:
            pergunta3 = input("3. Você é a favor do voto obrigatório?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
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
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def get_pergunta4(self):
        loop = True
        while loop:
            pergunta4 = input("4. Você já tem a biometria cadastrada?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
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
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def get_pergunta5(self):
        loop = True
        while loop:
            pergunta5 = input("5. Você acredita que a urna eletrônica é confiável?\n[1] - Sim\n[2] - Não\n[3] - Não sei responder\n")
            if pergunta5 == '1':
                self.pergunta5 = pergunta5
                print('Respostas registradas.Muito obrigado por sua colaboração!')
                loop = False
            elif pergunta5 == '2':
                self.pergunta5 = pergunta5
                print('Respostas registradas.Muito obrigado por sua colaboração!')
                loop = False
            elif pergunta5 == '3':
                self.pergunta5 = pergunta5
                print('Respostas registradas. Muito obrigado por sua colaboração!')
                loop = False
            else:
                print("Por gentileza, verifique sua resposta/ opções disponíveis e tente novamente!\n")

    def exportar_eleitor(self):
        return self.__dict__

class Registrar_dados():
    columns = ["hora", "idade", "genero", "cidade", "pergunta1", "pergunta2", "pergunta3", "pergunta4", "pergunta5"]
    def __init__(self):
        if not path.exists("pesquisa_eleitoral.csv"):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(r'pesquisa_eleitoral.csv', index = False, header=True)
    def criar_csv(self, lista_eleitores):
        df = pd.DataFrame.from_dict(lista_eleitores) 
        df.to_csv(r'pesquisa_eleitoral.csv', index = False, header=False, mode='a')



sistema = Sistema()
