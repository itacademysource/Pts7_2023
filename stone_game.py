import random

player_choice = input('Напишите Ваш вариант (камень/ножницы/бумага): ')

computer_choice_variants = 'камень', 'ножницы', 'бумага'
computer_result = random.choice(computer_choice_variants)  # Выбор компа

if player_choice.lower() == computer_result:  # Ничья
    print('Ничья')
# Победные варианты
elif player_choice.lower() == 'камень' and computer_result == 'ножницы':
    print('Победа!')
elif player_choice.lower() == 'ножницы' and computer_result == 'бумага':
    print('Победа!')
elif player_choice.lower() == 'бумага' and computer_result == 'камень':
    print('Победа!')
# Проигрыш
else:
    print('Проигрыш :(')
