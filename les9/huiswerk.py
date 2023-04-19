number = int(input("Noem een getal onder de 100: \n"))


if number > 50:
    f = open('huiswerktext.txt', 'wt', encoding='utf-8')
    f.write("Het getal was hoger dan 50!")
    f.close()
    print('Textbestand is gemaakt')
    
    
f = open('huiswerktext.txt','rt', encoding='utf-8')
text = f.read()
print(text)
