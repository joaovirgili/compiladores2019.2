import os

#################### Inicialização ####################

PALAVRAS_RESERVADAS = [
    ("programainicio", "programainicio"),
    ("execucaoinicio", "execucaoinicio"),
    ("fimexecucao", "fimexecucao"),
    ("fimprograma", "fimprograma"),
    ("definainstrucao", "definainstrucao"),
    ("como", "como"),
    ("inicio", "inicio"),
    ("fim", "fim"),
    ("repita", "repita"),
    ("vezes", "vezes"),
    ("fimrepita", "fimrepita"),
    ("enquanto", "enquanto"),
    ("faca", "faca"),
    ("fimpara", "fimpara"),
    ("se", "se"),
    ("entao", "entao"),
    ("fimse", "fimse"),
    ("senao", "senao"),
    ("fimsenao", "fimsenao"),
    ("mova", "mova"),
    ("vire", "vire"),
    ("pare", "pare"),
    ("finalize", "finalize"),
    ("apague", "apague"),
    ("passo", "passo"),
    ("passos", "passos"),
    ("acenda", "acenda"),
    ("aguarde", "aguarde"),
    ("ate", "ate"),
    ("a", "a"),
    ("pronto", "pronto"),
    ("ocupado", "ocupado"),
    ("parado", "parado"),
    ("movimentando", "movimentando"),
    ("bloqueada", "bloqueada"),
    ("apagada", "apagada"),
    ("acessa", "acessa"),
    ("esquerda", "esquerda"),
    ("direita", "direita"),
    ("frente", "frente"),
    ("robo", "robo"),
    ("lampada", "lampada"),
    ("pronto", "pronto"),
    ("acesa", "acesa"),
    ("para", "para"),
    ("para", "para"),
]

SEPARADORES = [10, 32, 9]  # 32 = ESPAÇO, 9 = TAB, 10 = QUEBRA DE LINHA

full_path = os.path.realpath(__file__)
dir_nome = os.path.dirname(full_path)

f = open("lexico/casos-de-teste/in1", "r")

entrada = f.read()

saida = open("lexico/casos-de-teste/in1.out", "w")

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
        associacao = {tipo: id, "linha": LINHA_ATUAL}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
    elif(tipo == 'identificador'):
        identifiers.append(id)
        associacao = {tipo: id, "linha": LINHA_ATUAL}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
    elif(tipo == 'palavra_reservada'):
        reserved_words.append(id)
        associacao = {id[1]: id[1], "linha": LINHA_ATUAL}
        PILHA_DE_TOKENS.append(associacao)
        TABELA_DE_SIMBOLOS.append([associacao, LINHA_ATUAL])
        
#################### Funções de verificação ####################


# Verifica se é número
def isNumero(char):
    return ord(char) >= 48 and ord(char) <= 57

def isNumero0(char):
    return ord(char) == 48

def isPalavraReservada(char):
    for palavra_reservada in PALAVRAS_RESERVADAS:
        if char.lower() == palavra_reservada[1] or char.upper() == palavra_reservada[1]:
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
    FRASE_ATUAL = ''
    """while(isNumero0(entrada[POSICAO_ATUAL])):
        if(isUltimoCaractere()):
            break
        FRASE_ATUAL = entrada[POSICAO_ATUAL]
        avancaCaractere()"""
        
    while(isNumero(entrada[POSICAO_ATUAL])):
        if(isUltimoCaractere()):
            break
        FRASE_ATUAL += entrada[POSICAO_ATUAL]
        avancaCaractere()
        

    #verificar char apos o numero 
    if(isLetra(entrada[POSICAO_ATUAL])):
        printLinhaComErro("Numérico com caractere Letra")
        # quit()

    #gera erro ou empilha
    elif(isCharSeparador() or isUltimoCaractere()):
        #FRASE_ATUAL += entrada[POSICAO_ATUAL]
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
        if(isUltimoCaractere()):
            break
        FRASE_ATUAL += entrada[POSICAO_ATUAL]
        avancaCaractere()

    if(isCharSeparador() or isUltimoCaractere()):
        #FRASE_ATUAL += entrada[POSICAO_ATUAL]
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
        if(isUltimoCaractere()):
            break
    
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

def lexico() -> list:
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
    # printArquivoSaida()
    # print(PILHA_DE_TOKENS)
    # print(TABELA_DE_SIMBOLOS)
    saida.close()
    f.close()
    return PILHA_DE_TOKENS
    # quit()
