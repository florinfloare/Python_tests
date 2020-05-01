



print("Lista de la compra")

lista = []
input_de_usuario = None
while True:
    input_de_usuario = input("Que deseas comprar? ([Q] para salir): ")
    if input_de_usuario == "Q":
        break

    elif input_de_usuario in lista:
        print("{} ya se encuentra en tu lista de la compra".format(input_de_usuario))
    else:
            if input("Seguro que quieres añadir {} a la lista de la compra? [S/N]".format(input_de_usuario)) == "S":
                lista.append(input_de_usuario)


print("La lista de la compra es {}".format(lista))
