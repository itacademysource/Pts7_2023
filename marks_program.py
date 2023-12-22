marks = [7, 8, 9, 8, 8, 8, 7, 9, 10]

min_mark = min(marks)
max_mark = max(marks)

print(f'Минимальная оценка: {min_mark}')
print(f'Максимальная оценка: {max_mark}')

mark_sum = sum(marks)
count_marks = len(marks)

print(f'Средняя оценка: {mark_sum / count_marks:.1f}')
