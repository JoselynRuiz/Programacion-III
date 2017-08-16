def imprimir_lista(x):
    print("\nMi lista de supermecardo")
    artIndice = 0
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)

if __name__ == '__main__':
    lista = []

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
            if artInsertar not in lista:
                lista.append(artInsertar)
            else:
                print("Articulo ya esta en la lista")
        elif opc == 2:
            print("\nVamos a quitar un artuculo de la lista")
            artBorrar = input("Artuculo")
            if artBorrar in lista:
                lista.remove(artBorrar)
            else:
                print("\nLo siento. Articulo no encontrado")
        elif opc == 3:
            imprimir_lista(lista)
        #    print("Mi lista de supermecardo")
        #    for articulo in lista:
        #        print(articulo)
        elif opc == 4:
            break
        else:
            print("ERROR::Opcion no valida")
    print("Hasta luego")

