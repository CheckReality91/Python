#!/usr/bin/env python


def get_name():
    """
        Dit is een functie
    """
    # Vraagt de naam van de gebruiker.
    name = input("Wat is uw naam?: ")
    return name

def print_greeting(name):
    """
    Print een begroeting met de naam van de gebruiker naar het scherm.
    """
    print("Goedendag " + name + "!")

def main():
    print_greeting(get_name())

if __name__ == '__main__':
    main()
    
