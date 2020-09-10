#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("ECUACIÓN a X² + b X + c = 0")
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))
    c = float(input("Escriba el valor del coeficiente c: "))
    if a == b == c == 0:
        print("Todos los números son solución")
    elif a == b == 0:
        print("Sin solución")
    elif a == 0:
        print("Una solución: {}".format(- c / b))
    else:
        d = b*b - 4*a*c
        if d < 0:
            print("Sin solución real")
        elif d == 0:
            print("Una solución: {}".format(- b / (2*a)))
        else:
            print("Dos soluciones: {} y {}".format((-b - d**0.5) / (2*a) , (-b + d**0.5) / (2*a)))
if __name__ == "__main__":
    main()

