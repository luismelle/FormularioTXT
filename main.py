# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import os.path
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime #IMPORTA DATA ATUAL PARA VALIDAR DATA DIGITADA

kivy.require("1.9.0")

#ARRUMA ERRO UTF-8
import _locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

#CRIA AS ABAS NA TELA CForm
class Abas(TabbedPanel):
    def muda(self): #CRIA OS ANOS PARA O CAMPO SPINNER ANO
        var=[]
        for ano in range(2017, 1899, -1):
            var.append(str(ano))
        self.ids.ano.values = var

#CRIA A TELA COM O FORMULARIO
class Formular(Screen):
    pass

#CRIA A TELA DE POPUP
class CustomPopup(Popup):
    pass

#CRIA TELA PRINCIPAL
class CIniciar(Screen):
    pass

#CRIA TELA ONDE CONTEM AS ABAS E O FORMULARIO
class CForm(Screen):
    pass

class Resultado(BoxLayout):
    pass

class ScreenManage(ScreenManager):

    def troca_iniciar(self):
        self.current = 'Iniciar'

    def troca_pedido(self):
        self.current = 'Form'

    def open_popup(self, n):#DEFINE O TEXTO DO POPPUP DE ACORDO COM A VALIDAÇÃO
        the_popup = CustomPopup()
        if (n == 0):
            the_popup.title = 'SALVO'
            the_popup.title_color = 0, 1, 0, 1
        elif (n ==1):
            the_popup.title = "ERROR - JA POSSUI UM ARQUIVO COM ESTE NOME"
            the_popup.title_color = 1, 0, 0, 1
        else:
            the_popup.title = "ERRO AO SALVAR O ARQUIVO"
            the_popup.title_color = 1, 0, 0, 1
        the_popup.open()

    def salva(self, nome, end, dia, mes, ano, sexo, cpf, arq):#FAZ VALIÇÃO E SALVA
        try:
            if(os.path.exists(arq + '.txt')):#VERIFICA SE EXISTE ARQUIVO COM O NOME ESCOLHIDO
                n=1
                self.open_popup(n)
            else: #CASO NAO EXISTA CRIA ARQUIVO E SALVA
                n=0
                arquivo = open(arq+'.txt', 'a')
                arquivo.write(nome+"\n")
                arquivo.write(end+"\n")
                arquivo.write(sexo+"\n")
                arquivo.write(dia+"/"+mes+"/"+ano+"\n")
                arquivo.write(cpf+"\n")
                self.open_popup(n)
        except OSError:#VERIFICA ERRO DE OS
            self.open_popup(3)

class Formulario(App):
    def build(self):
        self.root = ScreenManage()
        return self.root

if __name__ == '__main__':
    Formulario().run()