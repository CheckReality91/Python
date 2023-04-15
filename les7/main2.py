fruit = "Appel Banaan Kiwi Grapefruit Kokosnoot Tomaat Druif Aardbei Peer Physalis"
fruit_list = fruit.split()

count = 0
for fruit in fruit_list:
    if count < 5:
        print(fruit)
        count += 1