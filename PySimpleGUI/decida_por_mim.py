#Projeto 5 - Decida por Mim 
#Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso não!',
            'Acho que está na hora certa!'
        ]

    def Iniciar(self):
        # Layout
        layout = [[sg.Text('Faça sua pergunta: ',size=(20,0))],
                  [sg.Input(size=(40,0),key='pergunta')],
                  [sg.Button('Decida por mim!')],
                  [sg.Output(size=(39,10),key='output')],
                  [sg.Button('Faça nova pergunta'), sg.Button('Fechar')]
                  ]
        # Cirar a janela
        window = sg.Window('Decida por mim', layout=layout)
        # Ler valores
        while True:
            event, values = window.read()
            # Fazer algo
            if event in (None, 'Fechar'):
                break
            elif event == 'Decida por mim!':
                resposta = random.choice(self.respostas)
                window['output'].update(resposta)
            elif event == 'Faça nova pergunta':
                window['output'].update('')
                window['pergunta'].update('')
        window.close()

decida = DecidaPorMim()
decida.Iniciar()
