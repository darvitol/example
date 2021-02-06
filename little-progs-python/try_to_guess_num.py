import random

res = False
rand = random.randint(1, 5)
while not res:
    num = int(input("Введите число: "))

    if num > rand:
        print("Число, что Вы пытаетесь угадать, МЕНЬШЕ")
    elif num < rand:
        print("Число, что Вы пиытаетесь угадать, БОЛЬШЕ")
    else:
        print("Вы угадали")
        res = True
