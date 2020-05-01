from random import randint
import os

vida_pikachu = 80
vida_squirtle = 90
vida_pikachu_actual = vida_pikachu
vida_squirtle_actual = vida_squirtle
tamaño_barra_vida = 20
while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelve el combate
    # Ataca Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Trueno")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca Onda Voltio")
        vida_squirtle -=11

    barras_de_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / vida_pikachu_actual)
    print("Pikachu:    [{}{}][{}/{}".format("*" * barras_de_vida_pikachu, " " * (tamaño_barra_vida - barras_de_vida_pikachu),vida_pikachu,vida_pikachu_actual))

    barras_de_vida_squirtle =int(vida_squirtle * tamaño_barra_vida / vida_squirtle_actual)
    print("Squirtle:   [{}{}][{}/{}]".format("*" * barras_de_vida_squirtle," " * (tamaño_barra_vida - barras_de_vida_squirtle),vida_squirtle,vida_squirtle_actual))

    input("Enter para continuar...\n")
    os.system("cls")
    # Ataca Squirtle
    print("Turno de ataque squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["p", "a", "b", "n"]:
        ataque_squirtle = input("¿Que ataca deseas realizar? [p]lacaje, pistola [a]gua, [b]urbuja, [n]ada ")

    if ataque_squirtle == "p":
        print("Squirtle ataca con placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "a":
        print("Squirtle ataca con pistola agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "b":
        print("Squirtle ataca con burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "n":
        print("Squirtle no hace nada")

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0
    barras_de_vida_pikachu = int(vida_pikachu * tamaño_barra_vida / vida_pikachu_actual)
    print("Pikachu:    [{}{}][{}/{}".format("*" * barras_de_vida_pikachu, " " * (tamaño_barra_vida - barras_de_vida_pikachu),
                                            vida_pikachu, vida_pikachu_actual))

    barras_de_vida_squirtle = int(vida_squirtle * tamaño_barra_vida / vida_squirtle_actual)
    print("Squirtle:   [{}{}][{}/{}]".format("*" * barras_de_vida_squirtle, " " * (tamaño_barra_vida - barras_de_vida_squirtle),
                                             vida_squirtle, vida_squirtle_actual))

    input("Enter para continuar...\n")
    os.system("cls")

if vida_pikachu > vida_squirtle:
        print("Pikachu gano la batalla")
else:
        print("Squirtle gano la batalla")


