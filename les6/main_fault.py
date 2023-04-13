"""
Huiswerk voor les 6 van het vak Python voor NHA Software Ontiwikkelaar

Dit is de foutieve module voor mijn huiswerkopdracht.

Er wordt een KeyError geprint omdat de Key niet in de dictionary voorkomt.


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
    menu = weekmenu[dag_van_de_week]
    print(f"Vandaag staat op het menu: {menu}")  
     

def main():
    get_menu()

if __name__ == "__main__":
    main()