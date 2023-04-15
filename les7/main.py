fruit = "Appel Banaan Kiwi Grapefruit Kokosnoot Tomaat Druif Aardbei Peer Physalis"
fruit = fruit.split()
iterator = iter(fruit)

count = 0
while count < 5:
    print(next(iterator))
    count += 1


