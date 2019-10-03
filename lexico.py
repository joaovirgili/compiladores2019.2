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
    ("instrucao", "vire"),
    ("instrucao", "pare"),
    ("instrucao", "finalize"),
    ("instrucao", "apague"),
    ("instrucao", "apagar"),
    ("instrucao", "passo"),
    ("instrucao", "passos"),
    ("instrucao", "acenda"),
    ("instrucao", "aguarde"),
    ("instrucao", "ate"),
    ("a", "a"),
    ("condicao", "pronto"),
    ("condicao", "ocupado"),
    ("condicao", "parado"),
    ("condicao", "movimentando"),
    ("condicao", "bloqueada"),
    ("condicao", "apagada"),
    ("condicao", "acessa"),
    ("sentido", "esquerda"),
    ("sentido", "direita"),
    ("frente", "frente"),
    ("robo", "robo"),
    ("lampada", "lampada"),
    ("pronto", "pronto"),
    ("acesa", "acesa"),
    ("para", "para"),
]

SEPARADORES = [10, 32, 9]  # 32 = ESPAÇO, 9 = TAB, 10 = QUEBRA DE LINHA
f = open("casos-de-teste/in3", "r")
entrada = f.read()

saida = open("casos-de-teste/in3.out", "w")

INPUT_TAM = entrada.__len__()
LINHA_ATUAL = 0
COLUNA_ATUAL = 0
POSICAO_ATUAL = 0
CHAR_ATUAL = ''

PILHA_DE_TOKENS = []
TABELA_DE_SIMBOLOS = []
numbers = []
reserved_words = []
identifiers = []

FLAG_ERRO = False


#################### Empilhando os tokens ######################
def empilha(id, tipo):
    if(tipo == 'numero'):
        numbers.append(id)
        associacao = {tipo + str(len(numbers)): id}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
    elif(tipo == 'identificador'):
        identifiers.append(id)
        associacao = {tipo+str(len(identifiers)): id}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
    elif(tipo == 'palavra_reservada'):
        reserved_words.append(id)
        associacao = {id}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
        
#################### Funções de verificação ####################


# Verifica se é número
def isNumero(char):
    return ord(char) >= 48 and ord(char) <= 57

def isPalavraReservada(char):
    for palavra_reservada in PALAVRAS_RESERVADAS:
        if char.lower() in palavra_reservada or char.upper() in palavra_reservada:
            return palavra_reservada

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

def isCharComentario():
    return entrada[POSICAO_ATUAL] == '#'

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
    FRASE_ATUAL = entrada[POSICAO_ATUAL]
    avancaCaractere()
    while(isNumero(entrada[POSICAO_ATUAL])):
        FRASE_ATUAL += entrada[POSICAO_ATUAL]
        avancaCaractere()

    #verificar char apos o numero 
    if(isLetra(entrada[POSICAO_ATUAL])):
        printLinhaComErro("Numérico com caractere Letra")
        # quit()

    #gera erro ou empilha
    elif(isCharSeparador() or isUltimoCaractere()):
        empilha(FRASE_ATUAL, 'numero')
    #comentario-erro
    elif(isCharComentario()):
        printLinhaComErro("Posição de comentário inválida. # apenas no início da linha")
    else:
        printLinhaComErro("Caractere desconhecido")
        # quit()
    


# Tratamento de token Identificador
def trataIdentificador():
    FRASE_ATUAL = entrada[POSICAO_ATUAL]
    avancaCaractere()

    while(isLetra(entrada[POSICAO_ATUAL]) or isNumero(entrada[POSICAO_ATUAL])):
        FRASE_ATUAL += entrada[POSICAO_ATUAL]
        if(isUltimoCaractere()):
            break
        avancaCaractere()

    if(isCharSeparador() or isUltimoCaractere()):
        x = isPalavraReservada(FRASE_ATUAL) if True else False
        if(x):
            empilha(x, "palavra_reservada")
        else:
            empilha(FRASE_ATUAL, "identificador")
    #comentario-erro
    elif(isCharComentario()):
        printLinhaComErro("Posição de comentário inválida. # apenas no início da linha")
    else:
        printLinhaComErro("Caractere desconhecido")
        # quit() 



def trataComentario():
    #avanca linha
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL

    while(isQuebraLinha() == False):
        avancaCaractere()
    
    LINHA_ATUAL += 1
    COLUNA_ATUAL = 0
    POSICAO_ATUAL +=1

def trataSeparador():
    #avanca linha
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL

    while(isCharSeparador()):
        avancaCaractere()
    
    LINHA_ATUAL += 1
    COLUNA_ATUAL = 0
    POSICAO_ATUAL +=1


def printLinhaComErro(erroLabel):
    global LINHA_ATUAL, COLUNA_ATUAL, POSICAO_ATUAL, FLAG_ERRO
    FLAG_ERRO = True

    colunaErro = COLUNA_ATUAL

    linhaAux = LINHA_ATUAL
    linha = ''
    linhaErro = ''

    # pega inicio de linha
    while(COLUNA_ATUAL != 0):
        POSICAO_ATUAL -= 1
        COLUNA_ATUAL -= 1

    # pega linha com erro
    while(LINHA_ATUAL == linhaAux):
        if (entrada[POSICAO_ATUAL] != '\n'):
            linha += entrada[POSICAO_ATUAL]
        if(COLUNA_ATUAL == colunaErro):
            linhaErro += "|"
        else: 
            linhaErro += " "
        avancaCaractere()

    saida.writelines("ERRO({}:{}): {}".format(LINHA_ATUAL, colunaErro, erroLabel) + "\n") 
    saida.writelines(linha + "\n")
    saida.writelines(linhaErro + "\n")

def printArquivoSaida():
    if (not FLAG_ERRO):
        for i in PILHA_DE_TOKENS:
            saida.writelines(str(i) + "\n")    


# Avança para o próximo caracter
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

    elif(isCharSeparador()):
        a = 2 #faça nada
        
    else:
        printLinhaComErro("Caractere desconhecido")

    avancaCaractere()
printArquivoSaida()
# print(PILHA_DE_TOKENS)
# print(TABELA_DE_SIMBOLOS)
saida.close()
f.close()
