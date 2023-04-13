"""
Huiswerk voor les 6 van het vak Python voor NHA Software Ontiwikkelaar

In de variabel 'weekmenu' staat een dictionary met key:value pairs voor elke dag van de week met een bijhorend gerecht

dag_van_de_week vraagt de gebruiker om een dag van de week en slaat deze op. De input wordt omgezet in kleine letters

in get_menu() staat een try-except block die eerste de code uitvoert. als er een KeyError ontstaat (omdat de ingevoerd data in dag_van_de_week niet voorkomt in de dictionary weekmenu) wordt er in het except block een bericht geprint naar de console dat er geen dag is ingevoerd.
In de finaly block wordt het eind van het programma geprint.


"""
import os

weekmenu = {
    "maandag": "Pizza",
    "dinsdag": "Hamburger",
    "woensdag": "Pasta",
    "donderdag": "Boerenkool", 
    "vrijdag": "Spare ribs",
    "zaterdag": "Zalmfilet",
    "zondag": "Chuck Roast",
}

dag_van_de_week = input("Welke dag van de week is het?: ").lower()

def get_menu():
    try:
        menu = weekmenu[dag_van_de_week]
        print(f"Vandaag staat op het menu: {menu}")
    except KeyError:
        print('Er is geen dag van de week ingevoerd')
    finally:
        print('Einde van het programma')    

        

def main():
    get_menu()

if __name__ == "__main__":
    main()