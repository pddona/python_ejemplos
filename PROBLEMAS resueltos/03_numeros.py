#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("ORDENAR TRES NÚMEROS")
    primero = int(input("Introduzca el primer número: "))
    segundo = int(input("Introduzca el segundo número: "))
    tercero = int(input("Introduzca el tercer número: "))
    if primero <= segundo and primero <= tercero:
        menor = primero
        if segundo <= tercero:
            medio = segundo
            mayor = tercero
        else:
            medio = tercero
            mayor = segundo
    elif segundo <= primero and segundo <= tercero:
        menor = segundo
        if primero <= tercero:
            medio = primero
            mayor = tercero
        else:
            medio = tercero
            mayor = primero
    elif tercero <= primero and tercero <= segundo:
        menor = tercero
        if primero <= segundo:
            medio = primero
            mayor = segundo
        else:
            medio = segundo
            mayor = primero
    print("El número menor es {} , el medio es {} y el mayor es {}".format(menor,medio,mayor))


    
if __name__ == "__main__":
    main()
