#Limppiar Pantalla
import os
os.system("cls")

edad = int(input("Ingrese una edad: "))

if edad >= 0 and edad < 18:
    print("Es menor de edad")
elif edad >= 18:
    print("Es adulto joven")
else:
    print("Usted no ha nacido")

