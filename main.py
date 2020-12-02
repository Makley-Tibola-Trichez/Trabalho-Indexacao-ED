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
            except Exception:
                print(" Nome do arquivo ja existente!")
        conteudo = input(" Digite o conteudo do arquivo: ")
        escrevendoarquivo(nome, conteudo)
        input("Pressione ENTER para continuar!")
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
            time.sleep(1)
        
        gravar_dic_arquivo("dicionario.txt", dic)
        time.sleep(1)
    elif (opcao == 3):
        opcao2 = int(input(" Digite qual sua busca: "))

        if (opcao2 == 1):
            palavras = input(" O que deseja buscar: ").lower()
            busca = tokenizacao(palavras)
            if len(busca) == 0:
                print(" ERROR! O mínimo da busca OR é 1 palavra")
            else:
                busca = stemming(busca)

                termos_obtidos = set()
                for i in range(len(busca)):
                    arquivos_busca = dic[busca[i]]
                    termos_obtidos = encontrar_termos_union(arquivos_busca, termos_obtidos)

                print(sorted(list(termos_obtidos)))
                
            input("Pressione ENTER para continuar!")
            
        elif (opcao2 == 2):
            palavras = input(" O que deseja buscar: ").lower()
            busca = tokenizacao(palavras)
            if(len(busca) == 0):
                print(" ERROR! O mínimo da busca AND é 1 palavra")
            else:
                busca = stemming(busca)
                
                termos_obtidos = set()
                get_index = []
                for i in range(len(busca)):
                    get_index.append(dic[busca[i]])
                    
                for j in range(1, len(get_index)):
                    arquivos_busca = set(dic[busca[0]]).intersection(dic[busca[j]])
                    termos_obtidos = encontrar_termos_intersect(arquivos_busca, termos_obtidos)
                    print(arquivos_busca)
                
            input("Pressione ENTER para continuar!")
        else:
            opcaoInvalida()
    elif (opcao == 4):
        print(" Termo : Arquivos")

        for i in dic:
            print(i, dic[i], sep=' : ', end='\n')
        
        input("Pressione ENTER para continuar!")
    elif (opcao == 0):
        exit()
    else:
        opcaoInvalida()
