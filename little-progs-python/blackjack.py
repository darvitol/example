import random

cards = [6, 7, 8, 9, 10, 2, 3, 4, 11]

your_cards = []

answer_bool = None

while answer_bool not in (True, False):
    answer = input('\nСыграем в "Блэкджек"? (yes/no) - ')
    goals = 0
    if answer == 'no':
        print('До встречи!')
        break
    elif answer == 'yes':
        random.shuffle(cards)
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        print('Ваши карты:', your_cards)
        for i in your_cards:
            goals += i
            goals = 0
            answer_again = input("Ещё карту? (yes/no) - ")
            for i in your_cards:
                goals += i
            if answer_again == 'no':
                print("Ваш результат: ", goals)
                if goals < 21 or goals > 21:
                    your_cards = []
                    print('ПРОИГРЫШ. Your score:', goals)
                else:
                    your_cards = []
                    print('ВЫИГРЫШ. Your score:', goals)
                break
            elif answer_again == 'yes':
                goals = 0
                new = random.choice(cards)
                your_cards.append(new)
                print('Ваши карты:', your_cards)
                for i in your_cards:
                    goals += i
                continue
    else:
        print("Вы ввели неправильный ответ, попробуйте ещё раз")



