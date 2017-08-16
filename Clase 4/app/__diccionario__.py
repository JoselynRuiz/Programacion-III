def imprimir_lista(x):
    print("\nMi lista de supermecardo")
    artIndice = 0
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)

def imprimir_diccionario(w):
    print("\nMi lista de supermercado")
    for art, cant in w.items():
        print("Articulo: " + str(art) + "(cantidad: " + str(cant) + ")")

if __name__ == '__main__':
    diccionario = {}

    while True:
        print('LISTA DE SUPERMERCADO')
        print('1. agregar elemento')
        print('2. quitar elemento')
        print('3. ver lista')
        print('4. salir')
        try:
            opc = int(input("OPCION:"))
        except ValueError:
            opc = 0

        if opc == 1:
            print("\nVamos a ingresar un articulo a la lista")
            artInsertar = input("Articulo")
       #     if artInsertar not in lista:
            if artInsertar not in diccionario:
       #         lista.append(artInsertar)
                 diccionario[artInsertar] = 1
            else:
               # print("Articulo ya esta en la lista")
                 diccionario[artInsertar] += 1
        elif opc == 2:
            print("\nVamos a quitar un artuculo de la lista")
            imprimir_diccionario(diccionario)
            artBorrar = input("Artuculo")
            if artBorrar in diccionario:

                o = int(input("1. borrar todo\n2. Borrar cantidad exacta"))

        #        lista.remove(artBorrar)
        #    else:
        #        print("\nLo siento.iculo no encontrado")
        elif opc == 3:
           # imprimir_lista(lista)
            imprimir_diccionario(diccionario)

        elif opc == 4:

           break
        else:
            print("ERROR::Opcion no valida")
    print("Hasta luego")