import random


while True:
    player_choice = input('Орел (0) или решка (1). Введите Ваш выбор: ')
    toss_result = random.randint(0, 1)

    if player_choice == str(toss_result):
        print('Вы угадали!')
    else:
        print('Вы не угадали. Попробуйте еще раз')
