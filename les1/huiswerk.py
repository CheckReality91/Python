naam = input("Wat is uw naam?: ")
plaats = input("Wat is uw geboorteplaats?: ")
leeftijd = int(input("Wat is uw leeftijd?: "))


output = "Uw gegevens: \n Naam: {}\n Geboorteplaats: {} \n Leeftijd: {}"
print(output.format(naam, plaats, leeftijd))

leuke_grap = "Wat zegt een banaan tegen een aap? Helemaal niets, want bananen kunnen niet praten."

if leeftijd > 50:
    print("Hee! je bent ouder dan 50 jaar. Dan krijg je nu een leuke grap te zien!")
    print(leuke_grap)