# Variables
num = 17
print(num)
print(type(num))
num2 = 2.5
print(num2)

cadl = "UIP"
print(cadl)
cadl2 = 'Panama'
print(cadl2)
cadl3 = """"Este es un ejemplo
de una cadena de varias lineas..."""
print(cadl3)

s1 = True
s1 = False


        # Introduccion de datos
 #       nombre = input("Nombre: ")
 #       edad = int(input("Edad: "))

 #       print("Bienvenido," + nombre + ". Tienes " + str(edad) + " anios")


# ciclos
while (True):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    print("Bienvenido," + nombre + ". Tienes " + str(edad) + " anios")

    # Decisiones
    if (edad < 18):
        print("\nEstas castigado")
    elif (edad == 18):
        print("\nPuedes salir\t...\tPero ven temprano")
    else:
        print("\nLarga a trabajar")

    salida = input("Desea continuar(S/N): ")
    if salida.upper() != "S" or salida != "s":
        break

print('Ciao')
