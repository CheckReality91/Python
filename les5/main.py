"""
Huiswerk voor les 5 van het vak Python voor NHA Software Ontiwikkelaar

"""

weekmenu = {
    "maandag": "pizza",
    "dinsdag": "hamburger",
    "woensdag": "pasta",
    "donderdag": "uitsmijter",
    "vrijdag": "spare ribs",
    "zaterdag": "zalmfilet",
    "zondag": "chuck roast",
}

dag_van_de_week = input('Welke dag van de week is het?: ').lower()


print(f"Vandaag staat op het menu: {weekmenu[dag_van_de_week]}")