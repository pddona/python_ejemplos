#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("ECUACIÓN A X + B = 0")
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))

    if a == b == 0:
        print("Todos los números son solución o hay infinitas soluciones.")
    elif a == 0:
        print("La ecuación no tiene solución.")
    else:
        print("La ecuación tiene una solución: {}".format(-b/a))    
    
if __name__=="__main__":
    main()
