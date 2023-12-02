# print('Hello')
#
#
# num_1 = 5
# num_2 = 3
#
# print(num_1 + num_2 - num_2 - 25)
#
# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)  # умножение
# print(num_1 / num_2)  # деление с остатком
# print(num_1 // num_2)  # деление без остатка
# print(num_1 % num_2)  # остаток от деления
#
# name = 'Artem '
# last_name = 'Troshkin'
# print(len(name))


# age = input('Введите возраст: ')
#
# if int(age) >= 18:
#     print('Ты совершеннолетний')
# else:
#     print('Ты несовершеннолетний')

age = -5

if age <= 10:
    if age <= 0:
        print('Такого возраста не существует')
    else:
        print('Ты ребенок')

elif age >= 11 and age <= 20:
    print('Ты подросток')
elif age >= 21 and age <= 60:
    print('Ты взрослый')
else:
    print('Ты старик')
