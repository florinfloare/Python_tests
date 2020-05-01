
print("Bienvenido a tu simulador de telefono que necesitas\n")
print("Tienes que responder unas preguntas para saber que movil necesitas\n")

so = input("Que sistema operativo prefieres? (Android) (ios): ")
dinero = input("Tienes dinero para gastar en un movil? (Si) (No): ")
camara = input("Tiene gran importancia para ti la camara del telefono? (Si) (No): ")

if so == "Android" and dinero == "Si" and camara == "Si":
    print("El telefono adecuado para ti es el Google pixel xl")
elif so == "Android" and dinero == "No":
    print("El telefono ideal para ti es el Redmi Note 9S")
elif so == "ios" and dinero == "Si":
    print("Tu telefono adecuado es el Iphone 11 Pro Max")
elif so == "ios" and dinero == "No":
    print("Debes buscar en el mercado de telefonos de segunda mano")
else:
    print("Debes responder a las preguntas con las opciones indicadas")
