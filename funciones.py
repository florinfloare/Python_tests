



def dibujar_tabla_del_cinco():
    for i in range(11):
        print("5 * {} = {}".format(i,i*5))

dibujar_tabla_del_cinco()

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boom")
    print("Fin de la cuenta atras {}".format(num))
cuenta_atras(10)



def area_rectangulo(base,altura):
    return (base * altura)
print(area_rectangulo(15,10))



import math

def area_circulo(radio):
    return  (radio**2) * math.pi
print(area_circulo(5))

def relacion(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
         return 0

print( relacion(10, 5))
print( relacion(5,10))
print( relacion(5,5))


def intermedio(a,b):
    return ((a + b) / 2 )

print(intermedio(-12,24))