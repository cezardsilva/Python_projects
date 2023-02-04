# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
# teste-sincronizando!
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        
    def Iniciar(self):
        # cirar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos =='Sim' or self.eventos == 's':
                self.GerarValordoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos a sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

