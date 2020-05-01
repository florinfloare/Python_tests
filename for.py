
import string

texto_usuario = input("Introduzca un texto: ")
espacios = 0
comas = 0
puntos = 0
mayusculas = 0
for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ",":
        comas += 1
    elif letra == ".":
        puntos += 1
    elif letra in string.ascii_uppercase:
        mayusculas += 1


print("espacios: {}, comas: {}, puntos: {}, mayusculas {}".format(espacios, comas, puntos, mayusculas))



texto_usuario = int(input("Elige un numero para saber su tabla de multiplicacion: "))

multiplicacion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in multiplicacion:
    print(item * texto_usuario)