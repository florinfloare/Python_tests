

dolar_euro = 0.91
libra_euro = 1.18


opcion = input("Que conversion quiere realizar dolar a euro (D) o libra a euro (L): ")

cantidad = int(input("Que cantidad de divisa quiere trasformar en euros: "))


if opcion == "D":
    print("La suma en euros es: {}".format(cantidad * dolar_euro))
if opcion == "L":
    print("La suma en euros es: {}".format(cantidad * libra_euro))
elif opcion != "D" or "L":
    print("De momento el conversor solo trabaja con Libras y Dolares, proximamente habrá actualizaciones con nuevas divisas")
