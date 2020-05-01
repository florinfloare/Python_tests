import random

print("Bienvenidos al juego de adivinar numeros")

numero_ganador = random.randint(1, 100)
numero = int(input("Escoge un numero de 1 al 100: "))
if numero == numero_ganador:
    print("Enorabuena acertaste")
if numero != numero_ganador:
    print("Lo siento no acertaste")

if numero > 100:
    print("Te has pasado de listo, es entre el 1 y el 100")
if numero < 0:
    print("No entendiste el juego, hay que elegir un numero entre 1 y 100")
if numero == 600:
    print("Has elegido el numero de la bestia")


print("El numero ganador era: {}".format(numero_ganador) )