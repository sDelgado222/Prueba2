"""Escriba un programa que pregunte al usuario por el número
de horas trabajadas y el coste por hora. Después debe de
mostrar por pantalla la paga que le corresponde"""
#Problema 6
nombre=input("Digite el nombre: ")
ht =int(input("Digite el número de horas trabajadas: "))
ch =float(input("Digite el costo por horas: "))
paga = ht * ch
print("El salario de "+nombre+" es de: ",paga," colones")
