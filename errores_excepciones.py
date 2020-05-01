




while True:
    try:
        n = int(input("Introduce un numero: "))
        m = 4
        print("{} / {} = {}".format(n,m,n/m))

    except:
        print("Ha ocurrido un error, introduce bien el numero")
    else:
        print("Todo ha funcionado correctamente")
        break
    finally:
        print("Fin de la iteracion")


def mi_funcion(algo = None):
    if algo is None:
        raise ValueError
mi_funcion()