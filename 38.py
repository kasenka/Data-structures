# Необходимо отсортировать массив объектов по заданному критерию и вывести результат на экран.
# В зависимости от переданного параметра отсортировать массив объектов класса «Книга» по автору,
# названию или году издания, используя алгоритмы сортировки: пузырьковую, сортировку вставками и быструю сортировку.
# Сравнить время выполнения алгоритмов сортировки с помощью декоратора. Данные о книгах хранятся в файле.
import time

def time_of_function(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнилось за {end_time - start_time}")
        return result
    return wrapped


class Book:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.dict = {'autor': 1, 'title': 0, 'year': 2}
        self.sort = {'autor': len, 'title': len, 'year': int}

    def get(self):
        books = []
        with open(self.data, 'r') as file:
            for i in file:
                if '\n' in i:
                    i = i[:-1]
                books.append(i.split('/'))
        return books

    @time_of_function
    def bubble_sort(self):
        data = self.get()
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                if self.sort[self.key](data[j][self.dict[self.key]]) > self.sort[self.key](data[j+1][self.dict[self.key]]):
                    data[j], data[j+1] = data[j+1], data[j]

        return data

    @time_of_function
    def insertion_sort(self):
        data = self.get()
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and self.sort[self.key](data[j][self.dict[self.key]]) > self.sort[self.key](key[self.dict[self.key]]):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]
            left = []
            right = []
            for i in range(1, len(data)):
                if self.sort[self.key](data[i][self.dict[self.key]]) < self.sort[self.key](pivot[self.dict[self.key]]):
                    left.append(data[i])
                else:
                    right.append(data[i])
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    @time_of_function
    def time_quick(self, data):
        return self.quick_sort(data)


books = Book('38.txt','autor')
print(books.bubble_sort())
print(books.insertion_sort())

print(books.time_quick(books.get()))