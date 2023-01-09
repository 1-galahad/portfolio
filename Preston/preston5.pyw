import kivy

#>>>> CHAMAR O CEREBRO
#from ogpbrain import *
from ogpbrainCLASS import *


Bot = Chatbot('Preston')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

kivy.require('1.9.0')
#>>>>>>>>>>>>>
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

#>>>>>>>>>>>>>>>>

class Gerenciador(ScreenManager):
    pass


#class Inicial(Screen):
 #   def usuarionome(self):
 #       box = BoxLayout(orientation = 'horizontal')
 #       Nome = self.ids.Usernome.text
 #
 #       label = Label(text = 'l')
 #       box.add_widget(label)

class Menu(Screen):
    pass
class userhub(Screen): #ID: painel
    pass
#>>>
class opcoespainel(BoxLayout):
    pass
class layoutpainel(BoxLayout):
    pass
class avaliador(BoxLayout):
    pass

class test(TabbedPanel):
    pass
#>>>

class oprestonmesmo(Screen): #ID: principal
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):   #Define o esc para voltar
        if key == 27:
            App.get_running_app().root.current = "menu"
            return True

    def on_pre_leave(self): #Define o esc para sair
        Window.unbind(on_keyboard=self.voltar)

    def pegaessetxt(self): #Função chamada no botao submit do arquivo Prston.kv
        Usertexto = self.ids.USERinput.text #PEGA A ENTRADA DO USER na função text input do arquivo Preston.kv que tenha o ID: USERinput, depois define como Usertexto


        frase = Usertexto #Aqui o Preston vai ter que escutar da função USERinput do arquivo Preston.kv
        if 'o que é ' in frase:
            frase = frase[8:]

        if 'oq é ' in frase:
            frase = frase[5:]
            
        if 'o que eh ' in frase:
            frase = frase[9: ]

        frase = frase.lower() #assimila tudo aprendido como um
        frase = frase.replace('oq', 'o que')

        resp = Bot.pensa(frase)

        print('User: ' + Usertexto)
        Bot.fala(resp)

        if 'executa' in resp:
            resp = 'Agora mesmo!'



        self.ids.USERinput.text = ''  #ZERA O TEXTO
        self.ids.respostadopreston.text = resp

        if ('Tchau, Tchau!') in resp:
            Preston().stop()


class Preston(App):
    def build(self):
        return Gerenciador()

Preston().run()
