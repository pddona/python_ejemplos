#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():

    print("COMPROBADOR DE AÑOS BISIESTOS")
    fecha = int(input("Escriba un año y le diré si es bisiesto: "))

    if fecha % 400 == 0:
        print(f"El año {fecha} es un año bisiesto porque es múltiplo de 400.")
    elif fecha % 100 == 0:
        print(f"El año {fecha} NO es un año bisiesto porque es múltiplo de 100 "
              f"sin ser múltiplo de 400.")
    elif fecha % 4 == 0:
        print(f"El año {fecha} es un año bisiesto porque es múltiplo de 4.")
    else:
        print(f"El año {fecha} NO es un año bisiesto.")

if __name__=="__main__":
    main()
