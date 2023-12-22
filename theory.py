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

# age = -5
#
# if age <= 10:
#     if age <= 0:
#         print('Такого возраста не существует')
#     else:
#         print('Ты ребенок')
#
# elif age >= 11 and age <= 20:
#     print('Ты подросток')
# elif age >= 21 and age <= 60:
#     print('Ты взрослый')
# else:
#     print('Ты старик')

# a = 5
#
# while a < 10:
#     a += 1
#     print(a)

# import random
#
#
# print(random.random())  # Случайное число от 0 до 1
# print(random.randint(1, 10))
# print(random.randrange(1, 10, 2))
# choices = 'Artem', 'Vasya', 'John'
# print(random.choice(choices))
#
# a = [1, 2, 3, 4, 5, 6]
# random.shuffle(a)
# print(a)
#
# print(random.uniform(1, 10))


# for i in range(1, 1001):
#     print(i ** 1000)

# names = 'Artem', 'Max', 'John', 'Vasya'
# for name in names:
#     print(name)


# my_list = [1, 2, 3, 4, 5]
# print(my_list)
#
# my_list.append(6)  # Добавление элемента в конец списка
# print(my_list)
#
# names = ['Artem', 'Vasya', 'Kevin']
# print(names[0])
#
# names.append('John')  # Добавление элемента в конец списка
# print(names)
#
# names.insert(1, 'Vlad')  # Вставка
# print(names)
#
# del names[-1]  # Удаление по индексу
# print(names)
#
# deleted = names.pop(-1)  # Удаление по индексу с записью в переменную
# print(names)
# print(deleted)
#
# names.remove('Vlad')
# print(names)
#
# names = ['Artem', 'Vasya', 'Kevin', 'John', 'Vlad']
#
# # names.sort()  # Постоянная сортировка
# sorted_names = sorted(names)  # Временная сортировка
# print(names)
# print(sorted_names)
#
# names.reverse()  # Вывод списка в обратном порядке
# print(names)
#
# print(len(names))  # Определение длины списка

def hello():
    print('Hello World')
    print('My name is Artem')
    print('Nice to see you!')
    print('I love Python')


# hello()

def get_user(name, age):
    print(f'Привет, меня зовут {name}.')
    print(f'Мне {age}.')
    if age >= 18:
        print(f'{name} совершеннолетний')
    else:
        print(f'{name} несовершеннолетний')


# get_user(name='Artem', age=22)
# get_user(name='Vasya', age=10)
# get_user('Petya', 19)


def check_user(username, status='user'):
    if status == 'admin':
        print(f'{username} администратор')
    else:
        print(f'{username} не администратор')


check_user(username='test')
check_user(username='test_1', status='admin')
