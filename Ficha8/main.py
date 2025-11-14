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

#def bib()

#lista = [('a', 8), ('b', 9), ('a', 3)]
#agrupa_por_chave(lista)

#print(listar_baralho())
#print(baralhar(listar_baralho()))
#print(dicionario_palavras("Hello World World Hai"))


lista_livros = [{'titulo1':('autor1','editora1','cidade1','1999','paginas1','isbn1')},
                {'titulo2':('autor1','editora1','cidade1','2024','paginas1','isbn1')},
                {'titulo3':('autor1','editora1','cidade1','2001','paginas1','isbn1')},
                {'titulo4':('autor1','editora1','cidade1','2000','paginas1','isbn1')},]
