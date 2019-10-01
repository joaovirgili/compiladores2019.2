# TODO
# 1 - Ajustar os tokens compostos (por exemplo, "Vire Para" devem ser dois tokens)
# 2 - Implementar tratamento de identificador e numero.
# 3 - Exibição de erro léxico.
# 4 - Comparções não case sensitive
# 5 - Adicionar lista de tokens gerados


#################### Inicialização ####################

PALAVRAS_RESERVADAS = [
    ("programa", "programainicio"),
    ("programa", "execucaoinicio"),
    ("programa", "fimexecucao"),
    ("programa", "fimprograma"),
    ("declaracao", "definainstrucao"),
    ("declaracao", "como"),
    ("bloco", "inicio"),
    ("bloco", "fim"),
    ("iteracao", "repita"),
    ("iteracao", "vezes"),
    ("iteracao", "fimrepita"),
    ("laco", "enquanto"),
    ("laco", "faca"),
    ("laco", "fimpara"),
    ("condicional", "se"),
    ("condicional", "entao"),
    ("condicional", "fimse"),
    ("condicional", "senao"),
    ("condicional", "fimsenao"),
    ("instrucao", "mova"),
    ("instrucao", "passos"),
    ("instrucao", "vire para"),
    ("instrucao", "pare"),
    ("instrucao", "finalize"),
    ("instrucao", "apague lampada"),
    ("instrucao", "acenda lampada"),
    ("instrucao", "aguarde ate"),
    ("condicao", "robo pronto"),
    ("condicao", "robo ocupado"),
    ("condicao", "robo parado"),
    ("condicao", "robo movimentado"),
    ("condicao", "frente robo bloqueada"),
    ("condicao", "dirieta robo bloqueada"),
    ("condicao", "esquerda robo bloqueada"),
    ("condicao", "lampada acessa a grente"),
    ("condicao", "lampada acessa a esquerda"),
    ("condicao", "lampada acessa a direita"),
    ("condicao", "lampada apagada a frente"),
    ("condicao", "lampada apagada a esquerda"),
    ("condicao", "lampada apagada a direita"),
    ("sentido", "esquerda"),
    ("sentido", "direita"),
]

SEPARADORES = [10, 32, 9]  # 32 = ESPAÇO, 9 = TAB, 10 = QUEBRA DE LINHA
f = open("casos-de-teste/in1", "r")
entrada = f.read()

INPUT_TAM = entrada.__len__()
LINHA_ATUAL = 0
COLUNA_ATUAL = 1
POSICAO_ATUAL = 0
CHAR_ATUAL = ''

PILHA_DE_TOKENS = []
TABELA_DE_SIMBOLOS = []
num = []


#################### Empilhando os tokens ######################
def empilha(id, tipo):
    if(tipo == 'numero'):
        num.append(id)
        associacao = {'num' + str(len(num)): id}
        #adiciona na pilha de tokens
        PILHA_DE_TOKENS.append(associacao)
        #adiciona na tabela de simbolos com informacoes
        TABELA_DE_SIMBOLOS.append(['num' + str(len(num)), id, LINHA_ATUAL])
    if(tipo == 'letra'):
        a = 0

#################### Funções de verificação ####################


# Verifica se é número
def isNumero(char):
    return ord(char) >= 48 and ord(char) <= 57


# Verifica se é letra maiúscula
def isLetraMaiuscula(char):
    return ord(char) >= 65 and ord(char) <= 90


# Verifica se é letra minúscula
def isLetraMinuscula(char):
    return ord(char) >= 97 and ord(char) <= 122


# Verifica se é letra (maiúsucla ou minúscula)
def isLetra(char):
    return isLetraMinuscula(char) or isLetraMaiuscula(char)

# Verifica se o caractere atual é # (comentario) e se é inicio de frase
def isComentario(char):
    return (char == '#' and COLUNA_ATUAL == 0)

# Verifica se próximo caractere é uma quebra de linha
def isQuebraLinha():
    return ord(entrada[POSICAO_ATUAL]) == 10


# Verific se o caractere atual é o último da entrada
def isUltimoCaractere():
    return POSICAO_ATUAL == INPUT_TAM - 1


# Verifica se próximo caractere é um separador
def isProxCharSeparador():
    return ord(entrada[POSICAO_ATUAL + 1]) in SEPARADORES

def isCharSeparador():
    return ord(entrada[POSICAO_ATUAL]) in SEPARADORES


#################### Funções de tratamento de tokens ####################

# Tratamento de token Número
def trataNumero():
    # TODO
    a = 0 # Apenas para não ter que comentar o método inteiro
    
    FRASE_ATUAL = entrada[POSICAO_ATUAL]
    avancaCaractere()
    while(isNumero(entrada[POSICAO_ATUAL])):
        FRASE_ATUAL += entrada[POSICAO_ATUAL]
        avancaCaractere()
    #verificar char apos o numero 
    if(isLetra(entrada[POSICAO_ATUAL])):
        print("erro em linha: ", LINHA_ATUAL+1)
        print(printLinhaComErro(POSICAO_ATUAL))
        quit()
    #gera erro ou empilha
    empilha(FRASE_ATUAL, 'numero')
    


# Tratamento de token Identificador
def trataIdentificador():
    # TODO
    a = 0 # Apenas para não ter que comentar o método inteiro

def trataComentario():
    #avanca linha
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL

    while(isQuebraLinha() == False):
        avancaCaractere()
    
    LINHA_ATUAL += 1
    COLUNA_ATUAL = 0
    POSICAO_ATUAL +=1


def printLinhaComErro(posErro):
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL
    
    linhaAux = LINHA_ATUAL
    linha = ''
    #pega inicio de linha
    while(COLUNA_ATUAL != 0):
        POSICAO_ATUAL -= 1
        COLUNA_ATUAL -= 1

    #pega linha com erro
    while(LINHA_ATUAL == linhaAux):
        avancaCaractere()
        linha += entrada[POSICAO_ATUAL]
        if(POSICAO_ATUAL == posErro):
            linha += '(erro aqui?)'

    return linha



# Avança para o próximo caractere
def avancaCaractere():
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL

    if (isUltimoCaractere()):
        POSICAO_ATUAL += 1
        return

    if (isQuebraLinha()):
        LINHA_ATUAL += 1
        COLUNA_ATUAL = 0
    else:
        COLUNA_ATUAL += 1
    POSICAO_ATUAL += 1

        

while (POSICAO_ATUAL < INPUT_TAM):
    CHAR_ATUAL = entrada[POSICAO_ATUAL]
      
    if (isNumero(CHAR_ATUAL)):
        trataNumero()

    elif(isLetra(CHAR_ATUAL)):
        trataIdentificador()

    elif(isComentario(CHAR_ATUAL)):
        trataComentario()
        continue

    print(POSICAO_ATUAL)
    print((LINHA_ATUAL, COLUNA_ATUAL, CHAR_ATUAL))
    avancaCaractere()

print(PILHA_DE_TOKENS)
print(TABELA_DE_SIMBOLOS)
f.close()
