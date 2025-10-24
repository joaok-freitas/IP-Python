a = (1,2,3,30,50)

def soma (tup):
    b = 0
    for i in range (len(tup)):
        b += tup[i]
    return b
def somawhile (tup):
    i, b = 0, 0
    while i < len(tup):
        b += tup[i]
        i += 1
    return b


if __name__ == '__main__':
    print (f"For -", soma(a))
    print (f"While -",somawhile(a))