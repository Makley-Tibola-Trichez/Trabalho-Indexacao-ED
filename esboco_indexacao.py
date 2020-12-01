## Definindo as funções necessárias para o processo de INDEXACAO

import glob, os, codecs, sys

dic = dict()

stopwords = []
nome_arq = 'stopwords.txt'

arq = codecs.open(nome_arq, "r", "UTF-8")
linhas = arq.readlines()
for linha in linhas:    
    stopwords.append(linha.replace('\n', '').strip().lower())
arq.close()

def indexacao(doc, arq):
    # doc: list | arq: str (nome do arquivo)
    for palavra in doc:
        if palavra in dic:
            lista_docs = dic[palavra]
            lista_docs.append(arq)
        else:
            dic[palavra] = [arq]
    

def tokenizacao(doc_inicial):
  return doc_inicial.split(' ')

def substitui_especiais(token):
  return token.replace('á', 'a')

def remove_pontuacao(token):
  novo_token = ''
  pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~'
  
  for char in token:
    if char not in pontuacoes:
      novo_token = novo_token + char
  
  return novo_token

# como remover pontuações, caracteres especiais, case-sensitive? [normalizacao]
def normalizacao(lista): # retornar uma list
  nova_lista = []
  
  # inserir codigo
    
  return nova_lista  

def remove_stopwords(lista):
    nova_lista = []

    for token in lista:
        if token.lower() not in stopwords:
            nova_lista.append(token)

    return nova_lista


def remove_repetidas(lista):    
    ## usar a estrutura de Conjunto (set)
    pass

##
## Passar por todos os arquivos
##
for arq in glob.glob("docs/*.txt"):
    print("[{}]".format(arq))
    docTemporario = ''
    
    # Abrir arquivo
    f = codecs.open(arq, "r", "UTF-8")
    linhas = f.readlines()

    for linha in linhas:
        # remove espaços em branco no inicio e fim de cada linha lida
        docTemporario += linha.replace('\r\n',' ')
    f.close()

    docTemporario = tokenizacao(docTemporario)
    docTemporario = remove_stopwords(docTemporario)
    
    
    # chamar as demais etapas

    #print(sorted(docTemporario))
    
    indexacao(docTemporario, arq)        
    print()
    
print("BUSCAR PELA PALAVRA 'prisão':")
print(dic['prisão'])
#print(dic['furadeira'])

#print( set(dic['polícia']) & set(dic['fura


