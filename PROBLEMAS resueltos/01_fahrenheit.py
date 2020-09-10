#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT")
    celsius = float(input("Escriba una temperatura en grados Celsius: "))

    fahrenheit = 1.8 * celsius + 32

    print("{0} ºC son {1} ºF".format(celsius,fahrenheit))


if __name__ == "__main__":
    main()
