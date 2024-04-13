#Limppiar Pantalla
import os
os.system("cls")

#Etapa 1
print("bienvenido al mundo de la programacion")
nom = input("Para comenzar, ingresa tu nombre: ")
print(f"tu nombre es: {nom}")
print(f"Bienvenida {nom}")

#Etapa 3 
x = int(input("Ingrese un número: "))
resultado = (x**2 + 3*x + 1)/4
print(f"El resultado es: {resultado}")