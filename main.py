"""Fonction qui importe le module de la racine carree."""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """

    Retourne True ou False si c'est un nombre premier ou non.

    >>>isprime(1)
    False
    >>>isprime(4)
    False
    >>>isprime(7)
    True
    >>>isprime(0)
    False

    """
    premier = True
    if p in (0,1):
        premier = False
    for i in range(2,p):
        if p%i == 0 or sqrt(p)%i == 0:
            premier = False
    return premier

#### Fonction principale


def main():
    """

    Retourne tous les nombres premiers a partir de la fonction isprime qui determine 
    s'il est premier ou non.

    >>>main()
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 

    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
