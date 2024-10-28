# а) Напишите лямбда-функцию, которая принимает два аргумента и возвращает их произведение.
# б) Найдите числа, которые являются квадратами целых чисел, из заданного списка чисел, используя лямбда-функцию.
# в) Напишите программу для подсчёта целых чисел в заданном смешанном списке с помощью лямбда-функции.

# a
a = lambda x,y : x * y
print(a(3,5))

#b
def is_square(x):
    return x**0.5 % 1 == 0

sp = [9, 12, 49, 2, 81]

# print(list(filter(lambda x: is_square(x),sp)))
print(list(filter(lambda x: x**0.5 % 1 == 0,sp)))

#c
mixed_list = [1, 'hello', 3.5, 7, 'world', 10, 2.2, 15]

print(len(list(filter(lambda x: isinstance(x, int), mixed_list))))