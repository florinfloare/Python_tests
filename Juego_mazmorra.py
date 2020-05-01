import random

print("Bienvenidos al juego de la mazmorra\n"
      "Se ve una puerta al fondo y te decides iir hacia la puerta\n"
      "Aqui se ven dos puertas una puerta semi-abierta y un agujero en el suelo.")

opcion = input("[OPCION (A) PUERTA SEMIABIERTA] |[OPCION (B) AGUJERO EN EL SUELO]: ")
if opcion == "A":
    print("Entras por la puerta semiabierta y un gran leon te espera, ¿Que haces?: ")
    opcion = input("[OPCION (A) SALES CORRIENDO Y DEJAS AL LEON ATRAS] |[OPCION (B) TE ENFRENTAS AL LEON]:")
    if opcion == "B":
        print("Pierdes la pelea con el leon y aqui se acaba el juego\n FIN! ")
    if opcion == "A":
         print("Sigues por el unico camino que tienes y en esté camino ves un palo en el suelo, ¿Que haces?")
         opcion = input("[A] Coger el palo | [B] Ignorar el palo y seguir")
         if opcion == "A":
            print("coges el palo")
            palo_en_inventario = True

         if opcion == "B":
            print("No coges el palo")
            palo_en_inventario = False

            numero_rata = random.randint(1,100)
            print("En tu camino se entromete una rata gigante que te hace una pregunta a voces ¿Cuanto es 5 * {}".format(numero_rata))
            opcion = int(input("¿Cual es la respuesta?"))
            if opcion == 5 * numero_rata:
                print("La rata no soporta los listillos asi que decide matarte| FIN "
            if opcion != 5 * numero_rata:
                print("FIN")


if opcion == "B":
print("El aguejero en el suelo te lleva hasta la salida y queda finalizado el juego. FIN ")
