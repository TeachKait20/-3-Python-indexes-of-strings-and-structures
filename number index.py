# Попробуем повзаимодействовать с элементом по его индексу
number = 4
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Для примера, сначала обратимся к числу из переменной
print(number / 2, number // 2, number % 2)

# Теперь к списку numbers и цифре 4, которая находится под индексом 9
print(numbers[9])

# Проведём те же операции
print(numbers[9] // 2, numbers[9] / 2, numbers[9] % 2)
