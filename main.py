import glob, os, time, codecs, sys, nltk, pickle
from geral import *

dic = dict()

while(True):
    os.system('cls')
    print("""---------------------- INDEXACAO -----------------------
 1. Criar novo documento
 2. Indexar documentos '.txt' presentes na pasta docs/
 3. Realizar consultas
     1. Usando operador OR
     2. Usando operador AND
     3. Usando expressões booleanas
 4. Mostrar Índice Invertido (para debug / print)
 0. sair
--------------------------------------------------------""")
    opcao = int(input(" Digite sua opcao: "))

    if (opcao == 1):
        while(True):
            nome = input(" Digite o nome do arquivo (.txt): ")
            try:
                criandoarquivo(nome)
                break
            except:
                print(" Nome do arquivo ja existente!")
        conteudo = input(" Digite o conteudo do arquivo: ")
        escrevendoarquivo(nome, conteudo)
        time.sleep(2)
    elif (opcao == 2):
        dic = limpa_dic(dic)
        stopwords = abrir_stopwords()

        for arq in glob.glob("docs/*.txt"):
            print("[{}]".format(arq) + "\t- indexando!")
            docTemporario = ''

            f = codecs.open(arq, "r", "UTF-8")
            linhas = f.readlines()

            for linha in linhas:
                    linha = normalizacao(linha)
                    docTemporario += linha.replace('\r\n',' ')
            f.close()

            docTemporario = docTemporario.replace("-"," ")
            docTemporario = docTemporario.replace("  "," ")
            docTemporario = docTemporario.replace("   "," ")
            docTemporario = substituir_especiais(docTemporario)
            docTemporario = tokenizacao(docTemporario)
            docTemporario = remove_stopwords(docTemporario, stopwords)
            docTemporario = remove_numeros_extenso(docTemporario)
            docTemporario = stemming(docTemporario)
            docTemporario = remove_repetidas(docTemporario)

            indexacao(docTemporario, arq, dic)
            time.sleep(2)
        
        gravar_dic_arquivo("dicionario.txt", dic)
        time.sleep(3)
    elif (opcao == 3):
        opcao2 = int(input(" Digite qual sua busca: "))
        if (opcao2 == 1):
            lista = criar_lista(input(">>> "))
            
        elif (opcao2 == 2):
            pass
        elif (opcao2 == 3):
            pass
        else:
            opcaoInvalida()
    elif (opcao == 4):
        pass
    elif (opcao == 0):
        exit()
    else:
        opcaoInvalida()
