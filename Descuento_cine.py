

edad = int(input("Que edad tienes: "))
tipo_de_carnet = input("Tienes algun carnet (E para estudiante / P para pensionista / F para familia numerosa / N para nada: ")
if (25 <= edad <= 35 and tipo_de_carnet == "E") or edad < 10 or (edad >= 65 and tipo_de_carnet == "P") or (tipo_de_carnet == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica ningun descuento")
