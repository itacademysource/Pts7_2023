weight = input('Введите вес (кг): ')
height = input('Введите рост (м): ')

result = int(weight) / float(height) ** 2

print(f'Ваш индекс массы тела равен: {result:.1f}')
