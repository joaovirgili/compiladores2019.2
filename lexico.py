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


# Verifica se próximo caractere é uma quebra de linha
def isQuebraLinha():
    return ord(entrada[POSICAO_ATUAL]) == 10


# Verific se o caractere atual é o último da entrada
def isUltimoCaractere():
    return POSICAO_ATUAL == INPUT_TAM - 1


# Verifica se próximo caractere é um separador
def isProxCharSeparador():
    return ord(entrada[POSICAO_ATUAL + 1]) in SEPARADORES


#################### Funções de tratamento de tokens ####################


# Tratamento de token Número
def trataNumero():
    # TODO
    a = 0 # Apenas para não ter que comentar o método inteiro


# Tratamento de token Identificador
def trataIdentificador():
    # TODO
    a = 0 # Apenas para não ter que comentar o método inteiro


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

    print((LINHA_ATUAL, COLUNA_ATUAL, CHAR_ATUAL))
    avancaCaractere()

f.close()
