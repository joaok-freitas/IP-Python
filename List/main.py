def test(a):
    if a == 10:
        return
    print(a)
    test(a+1)

test(1)





'''
def posicoes_lista(values: list[int]=[], value:int= 0)-> list[int]:
    indexes = []
    for i, e in enumerate(values):
        if e == value:
            indexes.append(i)
    return indexes


values = [1,7,3,1,4,5,1]
indexes = posicoes_lista(values, 1)
print(indexes)
'''