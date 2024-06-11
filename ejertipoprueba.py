import os
import time
os.system("cls")

camaronm = 0
carnemon = 0
chapollo = 0
chacarne = 0
parrillada = 0
totalproductos = 0
subtotal = 0
total = 0
totaldescuento = 0

menu = True
while menu:
    print("=Shin Whe Wensha chinos=")
    print("-"*24)
    print("=Menú Delivery=")
    print("1. Camarón Mandarin \t $11.000")
    print("2. Carne Mongoliana \t $10.000")
    print("3. Chapsui pollo \t $9.500")
    print("4. Chapsui Carne \t $12.000")
    print("5. Parrillada China \t $15.000")
    print("6. Mostrar Boleta")
    print("7. Cancelar pedido")

    opcion = 0
    try:
        opcion = int(input("Elija una de las opciones disponibles: "))
    except:
        print("La opcion debe ser numerica...")

    if opcion < 1 or opcion > 7:
        print("La opción no esta disponible, seleccione nuevamente")
        time.sleep(2)
        os.system("cls")
    else:
        os.system("cls")
        if opcion == 1:
            camaronm += int(input("Cuantos quiere?: "))
        elif opcion == 2:
            carnemon += int(input("Cuantos quiere?: "))
        elif opcion == 3:
            chapollo += int(input("Cuantos quiere?: "))
        elif opcion == 4:
            chacarne += int(input("Cuantos quiere?: "))
        elif opcion == 5:
            parrillada += int(input("Cuantos quiere?: "))
        elif opcion == 6:


            menudescuento = True
            while menudescuento:
                print("descuentos disponibles")
                print("1. cliente frecuente \t 15%")
                print("2. tarjeta vecino \t \t 10%")
                print("3. adulto mayor \t \t 7$")
                print("4. no tengo")

                opciondes = 0
                try:
                    opciondes = int(input("ingrese una de las opciones disponibles: "))
                except:
                    print("opcion no valida...")
                    time.sleep(2)
                    os.system("cls")

                if opciondes < 1 or opciondes > 4:
                    print("no disponible")
                    time.sleep(2)
                    os.system("cls")
                else:
                    if opciondes == 1:
                        descuento = 0.15
                    elif opciondes == 2:
                        descuento = .01
                    elif opciondes == 3:
                        descuento = 0.07
                    elif opciondes == 4:
                        descuento =  0
                    else:
                        print("opcion no valida")
                    
                    menudescuento = False 

            totalproductos = camaronm + carnemon + chapollo + chacarne + parrillada
            subtotal = camaronm * 11000 + carnemon * 10000 + chapollo * 9500 + chacarne * 12000 + parrillada * 15000
            
            totaldescuento = subtotal * descuento
            total = subtotal - totaldescuento
            
            print("----- SHIN WHE WENCHSA -----")
            print("-"*45)
            print(f"Total productos = \t {totalproductos}")
            print("-"*45)
            if camaronm > 0:
                print(f"{camaronm} \t camaron mandarin \t {camaronm * 11000}")
            
            if carnemon > 0:
                print(f"{carnemon} \t carne mongoliana \t {carnemon * 10000}")
            
            if chapollo > 0:
                print(f"{chapollo} chapsui de pollo \t {chapollo * 9500}")

            if chacarne >0:
                print(f"{chacarne} chapsui carne \t {chacarne * 12000}")

            if parrillada > 0:
                print(f"{parrillada} parrillada china \t {parrillada * 15000}")

            print(f"subtotal: \t {subtotal}")
            print(f"descuento: \t {totaldescuento}")
            print("-"*45)
            print(f"total: \t \t {total}")
            print("-" * 45)
            print("=== ¡GRACIAS POR SU COMPRA! :D ===")


            input("")
        elif opcion == 7:
            menu = False
        else:
            print("intente nuevamente...")

menu = False 

            

    
