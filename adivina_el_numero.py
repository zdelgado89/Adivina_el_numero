from random import *

# entrada
X = int(input ("ingrese un numero del 1 al 10:"))

#proceso
numero_generado = randint(1, 10)
if X == numero_generado:
    print("el numero", str(X), "es igual a", str(numero_generado))
elif X < numero_generado:
    print("el numero", str(X), "es menor a", str(numero_generado))
else:
    print("el numero", str(X), "es mayor a", str(numero_generado))