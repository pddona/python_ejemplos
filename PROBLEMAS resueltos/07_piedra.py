#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():

    from random import choice

    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    i = choice(["PIEDRA", "PAPEL", "TIJERA"])
    j = choice(["PIEDRA", "PAPEL", "TIJERA"])

    print("Pepe ha sacado {}.".format(i))
    print("Juan ha sacado {}.".format(j))

    if i == j:
        print("Han empatado.")
    elif i == "PIEDRA" and j == "TIJERA":
        print("Ha ganado Pepe.")
    elif i == "TIJERA" and j == "PAPEL":
        print("Ha ganado Pepe.")
    elif i == "PAPEL" and j == "PIEDRA":
        print("Ha ganado Pepe")
    else:
        print("Ha ganado Juan.")
if __name__ == "__main__":
    main()
