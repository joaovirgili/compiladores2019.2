import json
import lexico_funcao

entradaLexico = lexico_funcao.lexico()

f = open('sintatico/rl_tableFINAL.json', 'r')
tabelaLR = json.loads(f.read())

f = open('sintatico/gramatica.json', 'r')
gramatica = json.loads(f.read())

# entradaLexico = [
#     {'programainicio': 'programainicio'},
#     {'definainstrucao': 'definainstrucao'},
#     {'identificador': 'Trilha'},
#     {'como': 'como'},
#     {'inicio': 'inicio'},
#     {'mova': 'mova'},
#     {'numero': '2'},
#     {'passos': 'passos'},
#     {'aguarde': 'aguarde'},
#     {'ate': 'ate'},
#     {'robo': 'robo'},
#     {'pronto': 'pronto'},
#     {'vire': 'vire'},
#     {'para': 'para'},
#     {'esquerda': 'esquerda'},
#     {'apague': 'apague'},
#     {'lampada': 'lampada'},
#     {'vire': 'vire'},
#     {'para': 'para'},
#     {'direita': 'direita'},
#     {'mova': 'mova'},
#     {'numero': '3'},
#     {'passos': 'passos'},
#     {'aguarde': 'aguarde'},
#     {'ate': 'ate'},
#     {'robo': 'robo'},
#     {'pronto': 'pronto'},
#     {'fim': 'fim'},
#     {'execucaoinicio': 'execucaoinicio'},
#     {'vire': 'vire'},
#     {'para': 'para'},
#     {'direita': 'direita'},
#     {'fimexecucao': 'fimexecucao'},
#     {'fimprograma': 'fimprograma'}
# ]

# entradaLexico = [
#     {'programainicio': 'programainicio'}
# ]

def trataShift(action, token, tokenIdx, tokenData):
    novoEstado = int(action[1:])
    pilha.append(token)
    pilha.append(novoEstado)

def trataReduce(action, token, tokenIdx, tokenData):
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
        trataShift(newAction, token, tokenIdx, tokenData)
    elif 'r' in newAction:
        trataReduce(newAction, token, tokenIdx, tokenData)
    else:
        printaErro(token, tokenIdx, tokenData)

def printaErro(token, tokenIdx, tokenData):
    ultimoTokenError = ""
    if tokenIdx > 0:
        ultimoTokenData = entradaLexico[tokenIdx - 1]
        ultimoToken = list(ultimoTokenData)[0]
        ultimoTokenError = f'após {ultimoToken}.'
    else:
        ultimoTokenError = "no começo do arquivo."
    linha = tokenData["linha"] + 1
    print(f'Erro sintático (linha {linha}): {token} não esperado.')
    quit()

def getTopoIdx():
    return len(pilha) - 1

pilha = []
pilha.append(0)

for tokenIdx in range(len(entradaLexico)):
    tokenData = entradaLexico[tokenIdx]
    estado = pilha[getTopoIdx()]
    token = list(tokenData)[0]
    action = tabelaLR[estado][token]

    if 's' in action:
        trataShift(action, token, tokenIdx, tokenData)
    elif 'r' in action:
        trataReduce(action, token, tokenIdx, tokenData)
    else:
        printaErro(token, tokenIdx, tokenData)
        # ultimoTokenError = ""
        # if tokenIdx > 0:
        #     ultimoTokenData = entradaLexico[tokenIdx - 1]
        #     ultimoToken = list(ultimoTokenData)[0]
        #     ultimoTokenError = f'após {ultimoToken}.'
        # else:
        #     ultimoTokenError = "no começo do arquivo."
        # linha = tokenData["linha"] + 1
        # print(f'Erro sintático (linha {linha}): "{token}" não esperado {ultimoTokenError}')
        # quit()



print("OK")
quit()

