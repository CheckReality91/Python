#!/usr/bin/env python3python
"""
Huiswerk les 4:

In de eerste regels zijn de variabelen ingevuld.

Hierna staan de functies die van elke variabele de ID, Type of lengte terugsturen

In main komt het programma in logische volgorde tot stand.

"""


s = 'Hallo, ik ben een string'
i = 191565168613
l = [1, 2, 3, 4, 5, 3453, 55432]


def show_id(var):
    # Returns ID of the input in stringformat
    return str(id(var))

def show_type(var):
    # Return the type of the input in string format
    return str(type(var))

def show_length(var):
    # Check if var is of type int (int types do not have a length)
    if isinstance(var, int):
        var = str(var)
        return str(len(var))
    else:
        return str(len(var))

def bericht(a, b, c):
    # Print the message
    print("Variabel s is een " + show_type(a) + " en zijn ID is " + show_id(a) + " met een lengte van "+ show_length(a) + " en de waarde van deze variabel is " + str(a)) 
    print("Variabel i is een " + show_type(b) + " en zijn ID is " + show_id(b) + " met een lengte van "+ show_length(b) + " en de waarde van deze variabel is " + str(b)) 
    print("Variabel l is een " + show_type(c) + " en zijn ID is " + show_id(c) + " met een lengte van "+ show_length(c) + " en de waarde van deze variabel is " + str(c)) 
         
def main():
    bericht(s, i, l)
   
    
if __name__ == '__main__':
    main()