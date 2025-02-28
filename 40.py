import math


# реализация класса двоичной кучи
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

    def filt(self, start, end):
        new_heap = [self.heapList[0]]

        for zn in self.heapList[1:]:
            if start <= zn <= end:
                new_heap.append(zn)

        self.heapList = new_heap
        self.currentSize = len(new_heap) - 1

        i = self.currentSize // 2 # восстанавливаем свойство кучи
        while i > 0:
            self.percDown(i)
            i = i - 1

    def __str__(self):
        if not self.currentSize:
            return f'Двоичная куча пуста'
        else:
            heap_str = ""
            height = int(math.log(self.currentSize, 2)) + 1
            for i in range(0, height):
                for j in range(2 ** i, min(2 ** (i + 1), self.currentSize + 1)):
                    heap_str += str(self.heapList[j]) + " "
                heap_str += "\n"
            return heap_str.strip()


#Работает система, которая отслеживает активность пользователей на веб-сайте.
# Каждый раз, когда пользователь посещает страницу, система создает запись с временной меткой.
# Реализовать структуру данных на основе двоичной кучи, которая будет поддерживать операции добавления записи
# и извлечения записей за определенный период времени.

import datetime

binaryheap = BinaryHeap()
binaryheap.insert(datetime.datetime(2024,5,2))
binaryheap.insert(datetime.datetime(2024,5,1))
binaryheap.insert(datetime.datetime(2024,5,10))
binaryheap.insert(datetime.datetime(2024,5,17))
binaryheap.insert(datetime.datetime(2024,5,20))

start = datetime.datetime(2024,5,1)
end = datetime.datetime(2024,5,17)

binaryheap.filt(start,end)
print(binaryheap)