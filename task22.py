# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


count = int(input('Введите кол-во чисел первого множества: '))
elem_1 = []
for _ in range(count):
    number = int(input("Введите число множества: "))
    elem_1.append(number)
print(elem_1)

count = int(input('Введите кол-во чисел второго множества: '))
elem_2 = []
for _ in range(count):
    number = int(input("Введите число множества: "))
    elem_2.append(number)
print(elem_2)

elem_1 = set(elem_1)
elem_2 = set(elem_2)

s_set = sorted(elem_1.intersection(elem_2))
print(*s_set)


# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)