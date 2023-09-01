import requests  # Importa a biblioteca requests para fazer requisições HTTP.
import PySimpleGUI as sg  # Importa a biblioteca PySimpleGUI para criar a interface gráfica.

layout = [  # Define o layout da janela utilizando uma lista de listas.
    [sg.Text("Digite um CEP: "), sg.InputText(key="-CEP-"), sg.Button("Buscar")],cd
    [sg.Output(size=(40, 20), key="-OUTPUT-")],
]

window = sg.Window("Consulta de CEP ", layout)  # Cria uma janela com o título "Consulta de CEP" e o layout definido.

while True:  # Inicia um loop infinito para manter a janela aberta.
    event, values = window.read()  # Lê os eventos e valores da janela e interrompe o looping aguardando uma ação.

    if event == sg.WINDOW_CLOSED:  # Verifica se o evento é o fechamento da janela.
        break  # Encerra o loop se a janela for fechada.
    window["-OUTPUT-"].update("")  # Limpa a janela de saida de dados sempre após uma ação

    cep = values["-CEP-"].replace("-", "")  # Obtém o valor digitado no campo de entrada e remove os traços.

    if cep.isnumeric() and len(cep) == 8:  # Verifica se o CEP contém apenas números e possui tamanho igual a 8.
        requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/")  # Faz a requisição ao serviço ViaCEP.
        result = requisicao.json()  # Converte a resposta da requisição para um dicionário Python.

        if "erro" in result:  # Verifica se a resposta contém a chave "erro" indicando um CEP inválido.
            print("CEP não encontrado.")  # Imprime uma mensagem de erro na saída.

        else:
            lista = [(chave, valor) for chave, valor in result.items()]
            for c in lista:
                print(f"{c[0].upper()} : {c[1].upper()}")  # Imprime o resultado da busca na saída.
    else:
        print("Erro, digite um CEP válido.")  # Imprime uma mensagem de erro caso o CEP seja inválido.

window.close()
