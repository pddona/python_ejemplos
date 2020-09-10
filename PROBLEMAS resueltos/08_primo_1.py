#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    import time
        
    print("NÚMERO PRIMO")
    numero = int(input("Escriba un número entero mayor que 1: "))
    inicio = time.time()
    if numero <= 1:
        print("¡Le he pedido un número entero mayor que 1!")
    else:
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 2:
            print("{} es primo".format(numero))

        else:
            print("{} no es primo".format(numero))
            
    final = time.time()
    print("Tiempo de ejecución = {} segundos".format(final-inicio))
if __name__ == "__main__":
    main()
