"""
Huiswerk voor les 5 van het vak Python voor NHA Software Ontiwikkelaar

In de variabel 'weekmenu' staat een dictionary met key:value pairs voor elke dag van de week met een bijhorend gerecht

dag_van_de_week vraagt de gebruiker om een dag van de week en slaat deze op. de ingevoerde string wordt omgezet naar alleen kleine letters.

Daarna komt een loop die de gebruiker opnieuw naar de dag van de week vraagt als het ingevoerde dag niet in de dictionary staat.

In het print functie wordt de tekst geprint met het gerecht van de dag die uit de dictionary wordt gehaald aan de hand van de key die de gebruiker heeft opgegeven.
"""

weekmenu = {
    "maandag": "Pizza",
    "dinsdag": "Hamburger",
    "woensdag": "Pasta",
    "donderdag": "Boerenkool", 
    "vrijdag": "Spare ribs",
    "zaterdag": "Zalmfilet",
    "zondag": "Chuck Roast",
}

dag_van_de_week = input('Welke dag van de week is het?: ').lower()

while dag_van_de_week not in weekmenu:
    print('Dit is geen dag van de week. Probeer het nog een keer')
    dag_van_de_week = input('Welke dag van de week is het?: ').lower()

print(f"Vandaag staat op het menu: {weekmenu[dag_van_de_week]}")
