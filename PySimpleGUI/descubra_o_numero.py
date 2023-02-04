# Projeto 3/2 - Chute um número
# Objetivo: Cirar um algorítimo que gere um valor aleatório e eu tenho que ficar tentando o número até acertar.
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = random.randint(0, 100)

    def Iniciar(self):
        layout = [[sg.Text('Seu Número:',size=(20,0))],
                  [sg.Input(size=(10,0),key='valorChute')],
                  [sg.Button('Chutar!')],
                  [sg.Output(size=(39,10),key='output')],
                  [sg.Button('Jogar Novamente'), sg.Button('Fechar')]
                  ]
        window = sg.Window('Chute o Número', layout=layout)
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Fechar'):
                break
            elif event == 'Chutar!':
                try:
                    valor_do_chute = int(values['valorChute'])
                    if valor_do_chute > self.valor_aleatorio:
                        print('Chute um valor mais baixo!')
                    elif valor_do_chute < self.valor_aleatorio:
                        print('Chute um valor mais alto')
                    elif valor_do_chute == self.valor_aleatorio:
                        print('PARABÉNS! VOCÊ ACERTOU!!!')
                except ValueError:
                    print('Favor digitar apenas números!')
                window['valorChute'].update('')
            elif event == 'Jogar Novamente':
                self.valor_aleatorio = random.randint(0, 100)
                window['output'].update('')
                window['valorChute'].update('')
        window.close()

chute = ChuteONumero()
chute.Iniciar()

'''
Alteraçõs do ChatGPT:
Gerei o número aleatório na inicialização, sem necessidade de chamar uma outra função.
Removi a variável valor_minimo pois não era utilizada.
Utilizei window.read() para ler os eventos e os valores, e não precisamos mais de uma função específica para isso.
Utilizei elif para verificar se o valor do chute é menor ou maior, o que torna o código mais conciso.
Utilizei try e except para tratar os erros de entrada e informar o usuário.
Adicionei a opção de sair do programa, caso o usuário clique no botão de fechar a janela.
Removi a impossibilidade de jogar novamente, caso queira jogar de novo é necessário rodar o código novamente.

Para fazer com que o número do input anterior apagasse automaticamente quando você clicasse na caixa de texto novamente, você pode adicionar a propriedade enable_events=True na criação do input, e no event loop verificar se o evento é 'valorChute' e limpar o valor do input com window['valorChute'].update('')'
Note que adicionei uma verificação de eventos logo no inicio do laço while e coloquei a limpeza do input antes do evento Chutar!, dessa forma o input sera limpo sempre que o usuário clicar nele. Além disso, adicionei a condição de sair do laço while quando o usuário acertar o número.
'''