#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
    segundos = int(input("Escriba una cantidad de segundos: "))

    horas = segundos // 3600
    resto_1 = segundos % 3600
    minutos = resto_1 // 60
    resto = resto_1 % 60

    print("{0} segundos son {2} horas, {1} minutos y {3} segundos".format(segundos,minutos,horas,resto))


if __name__ == "__main__":
    main()
