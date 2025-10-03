total = input("Escreva um número inteiro -> ")
res = ""
for single in total: #para cada digito no total
    if int(single) % 2 != 0: # se o digito dividido por 2 for diferente de 0 (impar)
        res = str(res)+str(single) #escreve o número mais o novo número
print (res)