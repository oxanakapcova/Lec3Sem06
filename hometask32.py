# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
#         0  1  2  3  4   5   6  7   8  9   10 11 12  13 14  15  16  17   18 19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,  0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def range_list(array, min_num, max_num):
    new_list = []
    for i in range(len(array)):
        if min_num <= array[i] <= max_num:
            new_list.append(i)
    return new_list


my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input('type min number: '))
max_number = int(input('type max number: '))
print(*range_list(my_list, min_number, max_number))
