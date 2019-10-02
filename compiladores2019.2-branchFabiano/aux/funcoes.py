### Funções de verificação ###


def isNumero(char):
    return ord(char) >= 48 and ord(char) <= 57


def isLetraMaiuscula(char):
    return ord(char) >= 65 and ord(char) <= 90


def isLetraMinuscula(char):
    return ord(char) >= 97 and ord(char) <= 122


def isLetra(char):
    return isLetraMinuscula(char) or isLetraMaiuscula(char)