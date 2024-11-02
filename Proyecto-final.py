edad = int(input("Digite su edad: "))
nombre = (input("Digite su nombre"))

if edad >= 18:
  print(f"{nombre} pagará 10000 colones")
elif edad >= 15:
  print(f"{nombre} pagará 7500 colones")
elif edad >= 10:
  print("f{nombre} pagará 5000 colones")
else:
  print(f"{nombre} pagará 3500 colones")
print("Gracias por su compra"
