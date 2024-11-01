"""Ejercicio de Prueba semana 4"""
"""Se desea saber si el # ingresado por el usuario es mayor a 100, si el # solicitado es mayor deberá mostrar el número - 100 y si es menor a 100 solo debe de mostrar el #.
no se podrá utilizar números menores a 0, en caso contrario debe de notificar el error existente"""
numero = float(input("Digite un número: "))
if numero > 100:
    numero = numero - 100
    print("El número es = ", numero)
if numero >= 0:
    print("El número es = ", numero)
else:
    print("El número ingresado no puede ser igual o menor a 0 ")