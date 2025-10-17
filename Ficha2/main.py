def alinea1():
    import math
    x = int(input("Valor do cateto 1 \n > "))
    y = int(input("Valor do cateto 2 \n > "))
    result = math.sqrt((x**2) + (y**2))
    print(result)

def alinea2():
    nota1 = float(input("Valor da primeira nota: "))
    nota2 = float(input("Valor da segunda nota: "))
    media = (nota1 + nota2)/2
    if media >= 9.5:
        print(f"Aprovado. Média de {media}")
    else:
        print(f"Reprovado. Média de {media}")

def alinea3():
    valor1 = float(input("Primeiro valor: "))
    valor2 = float(input("Segundo valor: "))
    if valor1 > valor2:
        print(f"{valor1} é o maior")
    elif valor2 > valor1:
        print(f"{valor2} é o maior")
    else:
        print("Valores iguais")

def alinea4():
    valor = int(input("Introduza valor entre 1-15: "))
    while valor < 1 or valor > 15:
        print("Valor invalido")
        valor = int(input("Introduza valor entre 1-15: "))
    while valor < 15:
        valor += 1
        print(f"{valor}")

def alinea5():
    valor = int(input("Introduza valor entre 1-15: "))
    while valor < 1 or valor > 15:
        print("Valor invalido")
        valor = int(input("Introduza valor entre 1-15: "))
    result = valor
    while valor < 15:
        valor +=1
        result = result + valor

    print(result)

def alinea6():
    divisor = 0
    total = 0
    while total < 500:
        valor = int(input("Introduza valor entre 1-100: "))
        if valor > 100:
            print("Valor invalido")
        else:
            total = total + valor
            divisor = divisor + 1

    print(f"Média de {total/divisor}")

def alinea7():
    quantity = int(input("Introduza a quantidade: "))
    basevalue = float(input("Valor de compra: "))
    if 500 <= quantity < 1000:
        discount = 0.05
    if quantity > 1000:
        discount = 0.08
    else:
        discount = 0

    if discount != 0:
        total = quantity * basevalue * (1-discount)
    else:
        total = quantity * basevalue

    print(f"Valor de compra: {total}")

if __name__ == '__main__':
    #alinea1()
    #alinea2()
    #alinea3()
    #alinea4()
    #alinea5()
    #alinea6()
    #alinea7()