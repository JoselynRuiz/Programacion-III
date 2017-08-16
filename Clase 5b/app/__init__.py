from app.__circulo__ import *

if __name__ == '__main__':
    print("CALCULADORA DEL CIRCULO")

    radio = float(input("radio: "))
    area = calcular_area(radio)
    imprimir_resultado(calcular_area(radio), calcular_circunferencia(radio))