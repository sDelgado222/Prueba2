"""Practica2 semana 3 Parte 1"""
examenes = int(input("Digite la cantidad de examenes realizados: "))
nota1 = int(input("Digite la nota del primer examen: "))
nota2 = int(input("Digite la nota del primer examen: "))
nota3 = int(input("Digite la nota del primer examen: "))
promedio = ((nota1+nota2+nota3)/examenes)
if promedio >= 70:
  print("Nota = ", round(promedio, 2),"-"+" Aprobó ")
if promedio >= 60:
    print("Nota = ", round(promedio, 2),"-"+" Ampliación ")
else:
    print("Nota = ", round(promedio, 2),"-"+" Reprobó ")
