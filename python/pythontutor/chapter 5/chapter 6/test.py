max = 0
summa = 0

while True:
    number = int(input())
    if number == 0:
        print("res is", summa)
        break
    elif number == max:
        max = number
        summa += 1
    elif number > max:
        max = number
        summa = 1
