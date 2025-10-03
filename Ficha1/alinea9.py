print ("Escreva 3")
x = int(input("Valor de X -> "))
y = int(input("Valor de Y -> "))
z = int(input("Valor de Z -> "))

if x >= y and x >= z:
    print("O maior número é: ", x)
elif y >=x and y >= z:
    print ("O maior número é: ", y)
elif z >=x and z >= y:
    print ("O maior número é: ", z)