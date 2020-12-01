import glob, os, time, codecs, sys

def opcaoInvalida():
    print("========================================================")
    print("                   opção invalida!")
    print("========================================================")
    time.sleep(2)

def lendoarquivo(nomeArquivo):
    docNormal = ''
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'r', "UTF-8")
    for linha in f:
        # remove espaços em branco no inicio e fim de cada linha lida
        docNormal += linha.strip()
    f.close()

    # print(docNormal)
    return docNormal

def lendoarquivos():
    for arq in glob.glob("docs/*.txt"):
        print("[{}]".format(arq))
        docTemporario = ''

        # Abrir arquivo
        f = codecs.open(arq, "r", "UTF-8")
        linhas = f.readlines()

        for linha in linhas:
            # remove espaços em branco no inicio e fim de cada linha lida
            docTemporario += linha.strip()
        f.close()

        print(docTemporario)
        print()

def criandoarquivo(nomeArquivo):
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'x', "UTF-8")
    f.close()

def escrevendoarquivo(nomeArquivo, texto):
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'w', "UTF-8")
    f.write(texto)
    f.close()

def remove_stopwords(lista):
    nova_lista = []

    for token in lista:
        if token.lower() not in stopwords and token.lower() != '':
            nova_lista.append(token)

    return nova_lista

def tokenizacao(doc_inicial):
    return doc_inicial.split(' ')


def substituir_especiais(token):
    for i in range(len(token)):
        if (token[i] == 'á' or token[i] == 'ã' or token[i] == 'â' or token[i] == 'à' or token[i] == 'ä'):
            token = token.replace(token[i], 'a')
        elif (token[i] == 'ç'):
            token = token.replace(token[i], 'c')
        elif (token[i] == 'é' or token[i] == 'ê' or i == 'ë'):
            token = token.replace(token[i], 'e')
        elif (token[i] == 'í' or token[i] == 'ï'):
            token = token.replace(token[i], 'i')
        elif (token[i] == 'ó' or token[i] == 'õ' or token[i] == 'ô' or token[i] == 'ö'):
            token = token.replace(token[i], 'o')
        elif (token[i] == 'ú' or token[i] == 'ü'):
            token = token.replace(token[i], 'u')

    return token

def remove_numeros(token):
    nova_lista = []
    lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(token)):
        if (token[i] not in lista_numeros):
            nova_lista.append(token[i])

    return nova_lista

def remove_numeros_extenso(lista):
    numeros_extenso = []
    nova_lista = []
    nome_arq = 'numeros.txt'

    arq = codecs.open(nome_arq, "r", "UTF-8")
    linhas = arq.readlines()
    for linha in linhas:    
        numeros_extenso.append(linha.replace('\n', '').strip().lower())
    arq.close()

    for token in lista:
        if token.lower() not in numeros_extenso and token.lower() != '':
            nova_lista.append(token)

    return nova_lista
    
def normalizacao(linha):
    token = ''
    nova_lista = []
    pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~'

    linhaFinal = substituir_especiais(linha)
    linhaFinal = remove_numeros(linhaFinal)
    
    for i in range(len(linhaFinal)):
        for j in linhaFinal[i]:
            if (j in pontuacoes):
                continue
            else:
                token += j.lower()
        nova_lista.append(token)
        retorno = "".join(nova_lista)
        token = ''
        
    return retorno

def remove_repetidas(lista):
    conjunto = set(lista)
    return conjunto

# """"""""""""""""""""""remove stopwords""""""""""""""""""""""""""""""
stopwords = []
nome_arq = 'stopwords.txt'

arq = codecs.open(nome_arq, "r", "UTF-8")
linhas = arq.readlines()
for linha in linhas:
    linha = substituir_especiais(linha)
    stopwords.append(linha.replace('\n', '').strip().lower())
arq.close()
# """"""""""""""""""""""remove stopwords""""""""""""""""""""""""""""""

docTemporario = ''
arq = "Docs/doc1.txt"
f = codecs.open(arq, "r", "UTF-8")
linhas = f.readlines()

for linha in linhas:
        # remove espaços em branco no inicio e fim de cada linha lida
        linha = normalizacao(linha)
        docTemporario += linha.replace('\r\n',' ')
f.close()

docTemporario = docTemporario.replace("  "," ")
docTemporario = docTemporario.replace("-"," ")
docTemporario = docTemporario.replace("   "," ")
docTemporario = tokenizacao(docTemporario)
docTemporario = remove_stopwords(docTemporario)
docTemporario = remove_numeros_extenso(docTemporario)
docTemporario = remove_repetidas(docTemporario)
print(docTemporario)

# ! primeiro  remove stopwords      ok
# ! segundo   substituir_especiais  ok
# ! terceiro  tokenizacao           ok
# ! quarto    remove_stopwords      ok
# ! quinto    normalizacao          ok
# ! sexto    indexacao             

