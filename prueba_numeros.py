


numero_usuario = input("introduzca los numeros separados por coma: ")
numeros =[int(numero) for numero in numero_usuario.split(",")]
print(max(numeros))
print(min(numeros))