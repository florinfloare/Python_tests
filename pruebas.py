import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("error - filas o columnas incorrectos")
        print("ejemplo: pruebas.py [1-9][1-9]")
    else:
        for f in range(filas):
            print()
            for c in range(columnas):
                print(" [] ", end="")

else:
    print("error - argumentos incorrectos")
    print("ejemplo: pruebas.py [1-9][1-9]")