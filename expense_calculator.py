# expense_calculator

def calculate_expenses(expenses: list):
    total_expenses = sum(expenses)

    max_expense = max(expenses)
    min_expense = min(expenses)

    average_expense = total_expenses / len(expenses)

    print(f'Общий расход: {total_expenses}')
    print(f'Максимальный расход: {max_expense}')
    print(f'Минимальный расход: {min_expense}')
    print(f'Средний расход: {average_expense:.2f}')


expenses = [10, 50, 50, 150, 280, 400, 100]
calculate_expenses(expenses=expenses)
