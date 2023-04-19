f = open('songtekst.txt', 'wt', encoding='utf-8')
f.write("I walk a lonely road, the only one that i have ever known.")
f.close()

text = input("Schrijf hier een tekst die opgeslagen wordt in een .txt bestand: \n")
f = open('text.txt', 'wt', encoding='utf-8')
f.write(text)
f.close()