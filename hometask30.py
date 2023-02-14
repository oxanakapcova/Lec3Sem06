# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def math_progression(first_element, step, amount):
    progression = [first_element]
    count = 0 # можно было через цикл for
    current_element = first_element
    while count != amount - 1:  # (потому что первый элемент уже есть
        progression.append(current_element + step)
        count += 1
        current_element = progression[count]
    return progression

def progression2(first_element, step, amount):
    new_list = []
    for i in range(amount):
         new_list.append(first_element + i * step)
    return (new_list)



a, b, c = 7, 3, 5  # int(input('first element: ')), int(input('difference: ')), int(input('amount: '))
print(*math_progression(a, b, c))
print(*progression2(a, b, c))
