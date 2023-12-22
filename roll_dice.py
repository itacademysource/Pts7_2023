import random


win_count = 0
lose_count = 0

while True:
    input('Нажмите Enter, чтобы бросить кости...')

    comp_dice_1 = random.randint(1, 6)
    comp_dice_2 = random.randint(1, 6)

    player_dice_1 = random.randint(1, 6)
    player_dice_2 = random.randint(1, 6)

    comp_total = comp_dice_1 + comp_dice_2
    player_total = player_dice_1 + player_dice_2

    print(f'У Вас выпало {player_dice_1} и {player_dice_2}. Сумма: {player_total}')
    print(f'У противника выпало {comp_dice_1} и {comp_dice_2}. Сумма: {comp_total}')

    if player_total == comp_total:
        print('Ничья')
    elif player_total > comp_total:
        print('Победа!')
        win_count += 1
    else:
        print('Поражение :(')
        lose_count += 1

    print(f'Побед: {win_count} | Поражений: {lose_count}')
    print()
