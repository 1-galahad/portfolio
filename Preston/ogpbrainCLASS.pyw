import json
import sys
import os
import subprocess as s

#>>>>>>>>>>

#>>>>>>>>>>>>>
#>>>>>> FALA
import pyttsx3
en = pyttsx3.init()
#>>>>>>

class Chatbot():
    def __init__(self, nome): #inicia junto
        try:
            memoria = open(nome+'.json', 'r')

        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["Lucas", "Caspian"] , {"oi": "Olá, qual o seu nome?","tchau":"tchau"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria) #primeiro item da lista vai ser a lista de conhecidos, o segundo será a lista de frases
        memoria.close()
        self.historico = [None, ]



    def escuta(self, frase = None):
        #Captura a resposta do usuario e preprocessando-a
        if frase == None:
            frase = input(">: ") #começa a ouvir

            frase = str(frase)

        if 'executa' in frase:
            return frase

        if 'o que é ' in frase:
            frase = frase[8:]
            return frase

        if 'oq é ' in frase:
            frase = frase[5:]
            return frase

        frase = frase.lower() #assimila tudo como um
        frase = frase.replace('eh', 'é') #verifica os sinonimos
        frase = frase.replace('oq', 'o que')
        return frase

    def pensa(self, frase):

        #processa o input recebido

        if frase in self.frases: #Se a frase é identificada no DB de frases
            return self.frases[frase] # Retorna a resposta gravada para ele [como frase]

        if frase == 'aprende':  #Se o comando dado for 'aprende'... Preston processa o script
            en.say('Digite a frase') #Fala
            en.runAndWait() #Retorna a fala
            chave = input("Digite a frase: ") #Pergunta o que deve aprender

            en.say('Digite a resposta') #Fala
            en.runAndWait() #Retorna a fala
            resp = input("Digite a resposta: ") #Pergunta qual a resposta para o aprendizado

            self.frases[chave] = resp
            self.gravaMemoria()
            return 'Aprendido'

        if self.historico[-1] == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase

        if frase == 'adeus':
            return 'Tchau, Tchau!'

        try:
            resp = str(eval(frase))
            return resp
        except:
            pass

        return ("[...]")


    def pegaNome(self, nome):

        if 'meu nome é ' in nome:
            nome = nome[11:]

        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Olá mestre '

        else:
            frase = 'É um prazer conhecer você '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome+'!'

    def gravaMemoria(self):
        memoria = open(self.nome+'.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):
        if "executa " in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            en.say('Agora mesmo!')
            en.runAndWait()

            if 'win' in plataforma:
                os.startfile(comando)
                print ("Preston: " + 'executa ' + comando)
                
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg - open', comando])
        else:
            print ("Preston: " + frase)

        self.historico.append(frase) #adiciona na lista historico
