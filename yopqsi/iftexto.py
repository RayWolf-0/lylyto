#Limppiar Pantalla
import os
os.system("cls")

user = input("Ingrese su usuario: ")
pas = input("Ingrese su contraseña: ")

if user == "lya" and pas == "carejeta":
    print("Usted es WinWolf")
else:
    print("Usuario Incorrecto")

edad = int(input("Ingrese su edad: "))

if edad == 22:
    print("Es la edad de winWolf")
else:
    print("No es la edad, clave bloqueda")