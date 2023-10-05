from random import randint
digit = ""
repetition = False
for _ in range(4):
    if not repetition:
        while True:
            i = str(randint(0,9))
            if not i in digit:
                break
    else:
        i = str(randint(0,9))
    digit += i
while True:
    question = input("Введите число:")
    b = 0
    c = 0
    for j in range(4):
        if digit[j] == question[j]:
            b += 1
        elif question[j] in digit:
            c += 1
    print(b, "быков", "и", c, "коров")
    if b == 4:
        print("Ура! Победа!")
        break