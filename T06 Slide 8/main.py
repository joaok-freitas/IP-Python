def find_max (lista):
    a = lista[0]
    for e in lista:
        if e > a:
            a = e
    return a

def find_min (lista):
    a = lista[0]
    for e in lista:
        if e < a:
            a = e
    return a

def multiply_list (lista, multiplier):
    for i, e in enumerate(lista):
        lista[i] = e * multiplier
    return lista
    # ou simplesmente -V
    # return [e * multiplier for e in lista]

def sum_list (lista):
    a = 0
    for e in lista:
        a += e
    return a

def check_equal (lista1, lista2):
    for e1 in lista1:
        for e2 in lista2:
            if e1 == e2:
                return True
    return False


lista_multiply = [1,2,3]
listing = [1,2,3,4,5,6,7,8,9]
listing2 = [-5,-2]
multiplicador = 5

print(find_max(listing))
print(find_min(listing))
print(multiply_list(lista_multiply, multiplicador))
print(sum_list(listing))
print(check_equal(listing, listing2))




#PASSAGEM POR VALOR
def test(a):
    a+=1
    print(a)
x = 1
test(x)
print(x)

#PASSAGEM POR REFERENCIA
def test(a):
    a[0] = 5
    print(a)

x = [2,2,2]
test(x)
print(x)