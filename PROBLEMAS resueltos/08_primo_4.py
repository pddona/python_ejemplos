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
        if numero == 1 or numero == 2 or numero == 3 or numero == 5 or numero == 7:
            print("{} es primo".format(numero))
        
        else:
            resto = numero % 10
            if resto == 0 or resto == 2 or resto == 4 or resto == 5 or resto == 6 or resto == 8:
                print("{} no es primo".format(numero))
            else: # resto == 1 , 3 , 7 , 9
                contador = 0
                limite = round(numero ** 0.5)
                for i in range(1, limite + 1):
                    if numero % i == 0:
                        contador = contador + 1
                        if contador > 1:######################
                            break  ###########################
                if contador == 1:
                    print("{} es primo".format(numero))
                else:
                    print("{} no es primo".format(numero))
            
    final = time.time()
    print("Tiempo de ejecución = {} segundos".format(final-inicio))
if __name__ == "__main__":
    main()
