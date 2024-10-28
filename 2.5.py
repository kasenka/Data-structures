
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        slot = self.hash_function(key)
        for pair in self.table[slot]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[slot].append([key, value])

    def find(self, key):
        slot = self.hash_function(key)
        for pair in self.table[slot]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        slot = self.hash_function(key)
        for i, item in enumerate(self.table[slot]):
            if item[0] == key:
                del self.table[slot][i]
                return

    def filt_key(self):
        even_hash_table = []
        odd_hash_table = []

        table = [j for i in self.table if len(i)> 0 for j in i if len(j)> 0]
        for item in table:
            if item[0]%2 == 0:
                even_hash_table.append((item[0], item[1]))
            else:
                odd_hash_table.append((item[0], item[1]))

        new_even_hash_table = HashTable(len(even_hash_table))

        for good in even_hash_table:
            new_even_hash_table.insert(good[0],good[1])

        new_odd_hash_table = HashTable(len(odd_hash_table))
        for good in odd_hash_table:
            new_odd_hash_table.insert(good[0],good[1])

        return new_even_hash_table, new_odd_hash_table


    def get(self, key):
        slot = self.hash_function(key)
        for item in self.table[slot]:
            if item[0] == key:
                return item[1]
        return None


# а) Создать класс «Товар» с полями «Название», «Цена» и «Количество».
# Создать хеш-таблицу для хранения объектов класса «Товар» по ключу — артикулу товара.

#A
class Good:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"Название - {self.name}, цена: {self.price}, колличество: {self.amount}"

list_of_goods = [
    Good('Сыр',300, 12094 ), Good('Молоко',79, 11110 ),
    Good('Курица',245, 10484 ),Good('Йогурт',47, 123 ),
    Good('Хлопья',113, 23333 ), Good('Пудинг',69, 1883 ) ]

import random

hash_table = HashTable(len(list_of_goods))

id = []
for good in list_of_goods:
    good_id = random.randint(100_000,999_999)
    id.append(good_id)
    hash_table.insert(good_id,good)
#
# for i in range(len(id)):
#     print(hash_table.get(id[i]))