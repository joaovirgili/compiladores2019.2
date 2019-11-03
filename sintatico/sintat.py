import json

f = open('sintatico/rl_tableFINAL.json', 'r')
tabelaLR = json.loads(f.read())

f = open('sintatico/gramatica.json', 'r')
gramatica = json.loads(f.read())

entradaLexico = [
    {'programainicio': 'programainicio'},
    {'definainstrucao': 'definainstrucao'},
    {'identificador': 'Trilha'},
    {'como': 'como'},
    {'inicio': 'inicio'},
    {'mova': 'mova'},
    {'numero': '2'},
    {'passos': 'passos'},
    {'aguarde': 'aguarde'},
    {'ate': 'ate'},
    {'robo': 'robo'},
    {'pronto': 'pronto'},
    {'vire': 'vire'},
    {'para': 'para'},
    {'esquerda': 'esquerda'},
    {'apague': 'apague'},
    {'lampada': 'lampada'},
    {'vire': 'vire'},
    {'para': 'para'},
    {'direita': 'direita'},
    {'mova': 'mova'},
    {'numero': '3'},
    {'passos': 'passos'},
    {'aguarde': 'aguarde'},
    {'ate': 'ate'},
    {'robo': 'robo'},
    {'pronto': 'pronto'},
    {'fim': 'fim'},
    {'execucaoinicio': 'execucaoinicio'},
    {'vire': 'vire'},
    {'para': 'para'},
    {'direita': 'direita'},
    {'fimexecucao': 'fimexecucao'},
    {'fimprograma': 'fimprograma'}
]

# entradaLexico = [
#     {'programainicio': 'programainicio'}
# ]

def trataShift(action, token):
    novoEstado = int(action[1:])
    pilha.append(token)
    pilha.append(novoEstado)

def trataReduce(action, token):
    linhaInstrucao = int(action[1:]) 

    instrucao = gramatica[linhaInstrucao]["token"]
    value = gramatica[linhaInstrucao]["value"]

    if value != "":
        num_consume = len(value.split(" "))

        for i in range(num_consume):
            pilha.pop()
            pilha.pop()
    
    ultimoEstado = pilha[getTopoIdx()]
    ultimoEstadoInstrucao = tabelaLR[ultimoEstado][instrucao]

    if ultimoEstadoInstrucao == "":
        print("Erro sintatico a")
        quit()


    estado = int(ultimoEstadoInstrucao)
    pilha.append(instrucao)
    pilha.append(estado)

    newAction = tabelaLR[estado][token]

    if 's' in newAction:
        trataShift(newAction, token)
    else:
        trataReduce(newAction, token)


def getTopoIdx():
    return len(pilha) - 1

pilha = []
pilha.append(0)

for token in entradaLexico:
    estado = pilha[getTopoIdx()]
    token = list(token)[0]
    action = tabelaLR[estado][token]

    if 's' in action:
        trataShift(action, token)
    elif 'r' in action:
        trataReduce(action, token)
    else:
        print(f'Erro sintático: "{token}" não esperado.')
        quit()



print("OK")
quit()

