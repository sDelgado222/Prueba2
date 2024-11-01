"""Escriba un programa que recibiendo el nombre de la persona,
la estatura en punto flotante, el peso en punto flotante,
retorne un mensaje saludanod a la persona por su nombre e
indicándole su IMC (Indice de Masa Corporal)."""
#Problema 5
nombre=input("Ingrese su nombre: ")
estatura =float(input("Digite su estatura: "))
peso =float(input("Digite su peso: "))
IMC = peso/(estatura**2) 
print("Hola "+nombre+" según su estatura ",estatura," cm y su peso ",peso," lo que da una IMC de ", ("{0:.2f}".format(IMC)))