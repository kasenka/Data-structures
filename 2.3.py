#Написать функцию, которая принимает на вход список слов и сортирует его по алфавиту с помощью алгоритма сортировки вставками.
# Функция должна возвращать отсортированный список.

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort(['a','c','b']))

# Написать метод класса «Товар», который сортирует список товаров по цене с помощью алгоритма быстрой сортировки.
# Метод должен изменять исходный список.

class Good:
    def __init__(self, name, price):
        self.name = name
        self.price =price

    def get(self):
        return f'name - {self.name}: price - {self.price}'

    @classmethod
    def quick_sort(cls,goods):
        if len(goods) <= 1:
            return goods
        pivot = goods[0]
        left = []
        right = []
        for i in range(1,len(goods)):
            if goods[i].price < pivot.price:
                left.append(goods[i])
            else:
                right.append(goods[i])
        return cls.quick_sort(left) + [pivot] + cls.quick_sort(right)

goods = [
    Good("Телефон", 10000),
    Good("Ноутбук", 50000),
    Good("Планшет", 20000),
    Good("Часы", 15000),
    Good("Наушники", 3000)
]

goods = Good.quick_sort(goods)

for i in goods:
    print(i.get())

# Написать функцию, которая принимает на вход список строк и сортирует его по длине
# строк с помощью алгоритма сортировки выбором. Функция должна возвращать отсортированный список.

sp = ['123','','123456']

def selection(arr):
    for i in range(len(arr)):
        min_ell = i
        for j in range(i+1, len(arr)):
            if len(arr[j]) < len(arr[min_ell]):
                min_ell = j
        arr[i], arr[min_ell] = arr[min_ell], arr[i]

    return arr

print(selection(sp))