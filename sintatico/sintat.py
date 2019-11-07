import json
import sys
import re

sys.path.insert(1, '../lexico/')
import lexico_funcao

import tabela_de_simbolos as ts
import no

symbol_table = []
nome_table = []
arvore = []
arvore_semantica = []
nome_table.append(ts.TabelaDeSimbolos())
symbol_table.append(nome_table[len(symbol_table)])
tokens_name = ['PROG', 'DECL', 'INSTR', 'BLOCO', 'COND', 'ITER', 'LACO', 'COMANDO', 'COMANDOS', 'IFELSE', 'IF', 'ELSE','SENTIDO']

class Node:
    def __init__(self, value=None, nome=None, children=None):
        if children is None:
            children = []
        self.value, self.nome, self.children = value, nome, children

#table.add(x,y)
#table.search(x)

entradaLexico = lexico_funcao.lexico()

f = open('rl_tableFINAL.json', 'r')
tabelaLR = json.loads(f.read())

f = open('gramatica.json', 'r')
gramatica = json.loads(f.read())

def percorreArvoreSemantica(node, file=None, _prefix="", _last=True):
    if node.nome == 'PRODUCAO':
        print(_prefix, "`- " if _last else "|- ", '|', sep="", file=file)
    else:
        print(_prefix, "`- " if _last else "|- ", node.nome, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        percorreArvoreSemantica(child, file, _prefix, _last)


def printaArvore(arvore):
    root = Node("PROG", 'PRODUCAO')
    print(root.__dict__)
    root.children = transformaFilhos(arvore)
    print(root.__dict__)
    percorreArvoreSemantica(root)
    pprint_tree(root)

def pprint_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.value, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)

def transformaFilhos(filhos):

    nodeFilhos = []

    for f in filhos:
        no = Node(f.chave, f.nome)
        if not hasattr(f, 'filhos') or len(f.filhos) == 0:
            no.children = []    
        else: 
            no.children = transformaFilhos(f.filhos)
        nodeFilhos.append(no)

    return nodeFilhos

def montaArvore(arvore):

    linha = ""

    for no in arvore:
        linha += no.chave + " | "
        if hasattr(no, 'filhos') and len(no.filhos) > 0:
            linha += montaArvore(no.filhos)

    return linha + "\n"
    

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
    # print(action, token, tokenIdx, tokenData, int(action[1:]))
    
    arvore_semantica.append(tokenData[token])
    
    global arvore
    arvore.append(no.No(token, tokenData[token]))

    novoEstado = int(action[1:])
    pilha.append(token)
    pilha.append(novoEstado) 

    count = 0
    idx_token = 0
    existe_token = True
#    if 'identificador' in tokenData.keys() or 'numero' in tokenData.keys():
#        print(token, tokenData)
    for t in symbol_table:
        if t.search(token):
            count = count + 1
            continue
        else:
            idx_token = count
            existe_token = False
            break

    if existe_token:
        #nome_table[len(symbol_table)] = ts.TabelaDeSimbolos()
        nome_table.append(ts.TabelaDeSimbolos())
        nome_table[len(symbol_table)].add(token, tokenData)
        symbol_table.append(nome_table[len(symbol_table)])
    else:
        symbol_table[idx_token].add(token,tokenData)


    #for t in symbol_table:
    #    print('Tabela: ', count)
    #    count = count + 1
    #    print(t.__dict__)

def trataReduce(action, token, tokenIdx, tokenData):
    linhaInstrucao = int(action[1:]) 

    instrucao = gramatica[linhaInstrucao]["token"]
    value = gramatica[linhaInstrucao]["value"]

    global arvore

    novoNo = no.No(instrucao, 'PRODUCAO')
    if value != "":

        num_consume = len(value.split(" "))

        filhos = []

        for i in range(num_consume):
            if len(arvore) == 0:
                print("Erro arvore vazia")
            else:
                filhos.append(arvore.pop())
            pilha.pop()
            pilha.pop()

        novoNo.filhos = list(reversed(filhos))
    arvore.append(novoNo)
    
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

# outputArvore = montaArvore(arvore)
# print(outputArvore)
#for x in arvore:
#    print(x.__dict__)


#Analise Semantica
semantica_string = ''
for i, word in enumerate(arvore_semantica):
    semantica_string = semantica_string + word
    if i != len(arvore_semantica):
        semantica_string = semantica_string + ' '


#regra semantica do vire para em sentidos opostos
x = re.search("vire para esquerda vire para direita", semantica_string)
x2 = re.search("vire para direita vire para esquerda", semantica_string)

#regra semantica para 2 ou mais declaracoes com mesmo nome
y = re.findall("definainstrucao [a-zA-Z]+", semantica_string)

mySet = set(y)
if len(mySet) == len(y):
    print("erro semantico: ha duas declaracoes de instrucoes com mesmo nome")

if x or x2:
    print('erro semantico: ha ocorrencia de vire para em sentidos opostos seguidas')
#print(semantica_string)


#prints das arvores
printaArvore(arvore)
print("OK")
quit()

