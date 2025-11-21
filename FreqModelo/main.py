def soma_impares(lista):
    soma = 0
    for num in lista:
        if num % 2 != 0:
            soma += num
    return soma

numeros = [5, 10, 15, 20, 25, 30]
print(soma_impares(numeros))

def calcular_expoente(base, expoente):
    if expoente == 0:
        return 1
    elif base == 0:
        return 0
    else:
        resultado = base
        for i in range (expoente-1):
            resultado = resultado * base
        return resultado
        #return base**expoente

print(calcular_expoente(4, 2))

def dicionario_medias(notas):
    medias = { }
    for aluno in notas:
        soma = 0
        for nota in notas[aluno]:
            soma += nota
        media = soma/len(notas[aluno])
        medias[aluno] = media
    return medias


notas = {"Joao":[15,16,14], "Maria":[18,17,19], "Pedro":[12,13,14]}
print (dicionario_medias(notas))