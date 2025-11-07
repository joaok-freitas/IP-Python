def remove_multiplos(listing, multiple):
    newlist = []
    for num in listing:
        if num % multiple != 0:
            newlist.append(num)
    return newlist

def junta_ordenadas(list1, list2):
    return sorted(list1+list2)

def duplica_elementos(listing):
    newlist = []
    for num in listing:
        newlist.append(num)
        newlist.append(num)
    return newlist

def cria_lista_multiplos(num):
    if type(num) != int:
        return "Valor inválido"
    newlist = []
    for e in range(10):
        newlist.append(e*num)
    return newlist

def substitui(listing, old, new):
    newlist = []
    for num in listing:
        if num == old:
            newlist.append(new)
        elif num != old:
            newlist.append(num)
    return newlist

def remove_repetidos(listing):
    newlist = []
    for num1 in listing:
        if num1 not in newlist:
            newlist.append(num1)
    return newlist

def posicoes_lista(listing, element):
    newlist = []
    for i, num in enumerate(listing):
        if num == element:
            newlist.append(i)
    return newlist

if __name__ == '__main__':
    lista = [2,3,5,9,12,33,34,45]
    lista2 = [0,1,100,200,300]
    lista_repeat = [1,2,3,1,1,1,2,3]
    multiplo = 3
    velho = 2
    novo = "a"
    lista_pos = ["a", 2, "b", "a"]
    elemento = "a"

    print(remove_multiplos(lista, multiplo))
    print(junta_ordenadas(lista,lista2))
    print(duplica_elementos(lista))
    print(cria_lista_multiplos(multiplo))
    print(substitui(lista, velho, novo))
    print(remove_repetidos(lista_repeat))
    print(posicoes_lista(lista_pos, elemento))