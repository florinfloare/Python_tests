texto_usuario = int(input("Elige un numero para saber su tabla de multiplicacion: "))

for n in range(1,11):
    if n % 2 == 0:
        print("{} x {} = {}".format(n, texto_usuario, n * texto_usuario ))






