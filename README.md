# Trabalho de compiladores 2019.2

## Gramática
- A gramática criado a partir da linguagem Robot-L está representada no arquivo "gramatica.txt".

## Léxico
- Todos os arquivos referente ao analisador léxico estão na pasta "lexico".
- Código fonte do analisador léxico: arquivo "lexico.py"
- Casos de teste estão na pasta "casos-de-teste"
- Imagens de análise de codigo correta e errada estão na pasta "imagens".
- Expressões regulares no arquivo "expressoes_regulares.txt"
- Autômato no arquivo "AUTOMATO.pdf"


## Sintático
- Todos os arquivos referenes ao analisador sintático estão na pasta "sintatico".
- Código fonte do analisador sintático: arquivo "sintatico/sintat.py"
- A gramática criada foi exportada para o formato JSON para facilitar a leitura da mesma no código do analisador sintático.
- O analisador léxico foi inserido na pasta do sintático para ser importada como uma função. No início do analisador sintático, a função léxico é chamada para obtem a tabela de símbolos e assim efetuar a análise sintática.


# Execução

- Certifique-se de ter o Python3 instaldo.

## Léxico
- Após clonar o repositório, edite o nome do arquivo de entrada e o nome do arquivo de saída que será gerado nas linhas 54 e 57, respectivamente.
- Basta executar "python3 lexico/lexico.py".
- Observe que o arquivo com o nome escolhido será gerado na pasta "casos-de-teste". Cuidado: caso o arquivo já exista, será gerado outro por cima.

## Sintático
- Após clonar o repositório, edite o nome do arquivo de entrada na linha 53 do arquivo sintatico/lexico_funcao.py para o arquivo de entrada de sua escolha. Por default, o arquivo "lexico/casos-de-teste/in1" é o selecionado.
- Basta executar o comando "python3 sintatio/sintat.py".

# Casos de teste

- O caso de teste possui uma entrada e por uma saída com nome igual porém com o sufixo ".out". Ex.: in1(entrada) e in1.out(saída)

# Equipe

- João Pedro Ache Virgili
- Fabiano Fernandes
- Alexandre Cury
