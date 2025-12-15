import random


def agrupa_por_chave(list):
    new_dictionary = {}
    for chave in list:
        if chave[0] not in new_dictionary:
            new_dictionary[chave[0]] = chave[1]
        else:
            new_dictionary[chave[0]] += new_dictionary[chave[1]]
    return new_dictionary

def listar_baralho():
    lista = []
    vlr = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    np = ["Espadas", "Copas", "Ouros", "Paus"]
    for i in np:
        for e in vlr:
            c = {i:e}
            lista.append(c)
    return lista

def baralhar(lista):
    for i, current_card in enumerate(lista):
        r=random.randint(0, len(lista) - 1)
        next_card = lista[r]
        lista[r] = current_card
        current_card = next_card
    return lista

def dicionario_palavras(string):
    words = string.split(" ")
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def bib(lista_livros):
    ano = 5000
    for livro in lista_livros:
        for titulo in livro:
            if livro[titulo][3] < ano:
                ano = livro[titulo][3]
                titulo_guardado = titulo
    return titulo_guardado, ano

def swap_dic(dic):
    newdic = {}
    for key in dic:
        for item in dic[key]:
            if item in newdic:
                newdic[item].append(key)
            else:
                newdic[item] = [key]
    return newdic


dic_letras = {"a":[1,2,3], "b":[2,4] ,"c":[2,8]}

#lista = [('a', 8), ('b', 9), ('a', 3)]
#agrupa_por_chave(lista)

#print(listar_baralho())
#print(baralhar(listar_baralho()))
#print(dicionario_palavras("Hello World World Hai"))


lista_livros = [{'titulo1':('autor1','editora1','cidade1',1999,'paginas1','isbn1')},
                {'titulo2':('autor2','editora2','cidade2',2024,'paginas2','isbn2')},
                {'titulo3':('autor3','editora3','cidade3',2001,'paginas3','isbn3')},
                {'titulo4':('autor4','editora4','cidade4',2000,'paginas4','isbn4')},]

#print(bib(lista_livros))
print(swap_dic(dic_letras))