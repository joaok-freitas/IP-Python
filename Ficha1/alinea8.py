print("Escolha um número de 1 a 5")
a = int(input("Número: "))
while a < 1 or a > 5:
    print("Número inválido")
    a = int(input("Número: "))
else:
    print(a)