from time import sleep

pedidos = {"Joao":[30,"Sushi"],
            "Pedro":[20,"Massa"],
            "Maria":[30,"Bife"],
            "Antonio":[0,"Sandes"]}

while pedidos:
    lista_a_remover = []
    for cliente in pedidos:
        if pedidos[cliente][0] > 0:
            print("Tempo de espera para", pedidos[cliente][1], "de", cliente, ">", pedidos[cliente][0],"minutos")
        else:
            print("Pedido",pedidos[cliente][1], "de", cliente, "está pronto")
            lista_a_remover.append(cliente)
    sleep(5)
    for cliente in lista_a_remover:
        del pedidos[cliente]
    for cliente in pedidos:
        pedidos[cliente][0] -= 5