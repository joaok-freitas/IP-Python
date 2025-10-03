print("Escreva um ano para eu dizer se é bissexto")
x = int(input("Ano -> "))
# x/4 naox/100 a nao ser x/400
if x%4 == 0 and x%100 != 0 or x%400 == 0:
    print(x, "é bissexto")
else:
    print(x, "não é bissexto")