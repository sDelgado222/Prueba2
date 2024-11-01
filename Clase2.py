"""
print("Hola Mundo")
print("Buenas ")
#Condicionales

== Igualdad
!= Diferencia
> mayor
< menor
>= mayor o igual
< menor o igual



nombre = input("Digite su nombre: ")

if ("steph"==nombre): # True o False
    print("El nombre es igual")
else:
    print("El nombre no es igual")

#Escribir un programa que pregunte al usuario su edad y muestre en pamtalla si es mayor de edad o no

edad=int(input("Digite su edad: "))

if edad>=18:
  print("Si es mayor de edad")
else:
  print("No es mayor de edad")

#Escriba un programa que solicite al usuario dos números y este devuelva su división. 
# Si el usuario introduce un 0 entonces debemos de indicarle que existe un error "División entre 0 no es posible"

num1=float(input("Digite el primer número: "))
num2=float(input("Digite el segundo número: "))

if(num1 !=0 and num2 !=0):
    division = num1/num2
    print("El resultado de la división es: ", division)
else:
    print("Error: división entre 0 no es posible")

#Escriba un programa que le solicite a un usuario que digite un número y que indique que es par o impar
num=int(input("Digite el número: "))

if num%2==0:
  print("El numero es par")
else:
  print("El número es impar")
  

# Escriba un programa para tributar un determinado impuesto se debe de ser mayor de 18 años y tener ingresos superiores a 500000 colones mensuales
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestr en pantalla si este usuario tributa o no
edad=int(input("Digite su edad: "))
num=float(input("Digite el monto de sus ingresos mensual: "))

if(edad >=18 and num >=500000):
    print("El usuario debe de tributar")
else:
    print("El usuario no debe de tributar")

  """
  
  #Escribir un programa para una sala de video juegos, si los usuarios tienen de menos de 10 años pagaran 3000 colones, si el usuario tiene 
  # menos de 15 años pagaran 5000 colones y el usuario tiene menos de 18 años va a pagra 7500 colones y si es mayor de edad entonces paga 10000 colones

edad = int(input("Digite su edad: "))

if edad >= 18:
  print("La persona pagará 10000 colones")
elif edad >= 15:
  print("La persona pagará 7500 colones")
elif edad >= 10:
  print("La persona pagará 5000 colones")
else:
  print("La persona pagará 3500 colones")

