import json

f = open('rl_table.json', 'r')
entrada = f.read()
entradaJson = json.loads(entrada)

tableLR = []
array = {}

for reg in entradaJson:
    for key in reg:
        b =(reg[key]).replace(u'\xa0', u' ')
        a =(key).replace(u'\xa0', u' ')
        #print(a, b)
        array[a] = b
    tableLR.append(array)
    array = {}

print(tableLR[1])

entradaLexico = 'programainicio'

pilha = []

pilha.append('$')
pilha.append(0)



quit()

