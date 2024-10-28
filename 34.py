from collections import deque

class Queue_0:
    def __init__(self,even_numbers = True):
        self.queue = []
        self.even_numbers = even_numbers

    def __str__(self):
        return str(self.queue)

    def enqueue(self, item):
        even = self.even_numbers  and item % 2 == 0
        odd = not self.even_numbers and item % 2 != 0
        if even or odd:
            self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return not len(self.queue)

    def size(self):
        return len(self.queue)

    def minimum(self):
        return min(self.queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, even_numbers = True):
        self.head = None
        self.tail = None
        self.even_numbers = even_numbers

    def is_empty(self):
        return not bool(self.head)

    def enqueue(self, data):
        even = self.even_numbers  and data % 2 == 0
        odd = not self.even_numbers and data % 2 != 0
        if even or odd:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node


    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self.head
        queue_str = ""
        while current:
            queue_str += " " + str(current.data)
            current = current.next
        return queue_str


# Создать класс очереди, который будет хранить только четные или только нечетные числа в зависимости от параметра,
# передаваемого при инициализации объекта класса очереди (True — хранить только четные числа, False — нечетные числа).
# При добавлении элемента, если его значение не соответствует заданному условию, то он не должен добавляться.

queue = Queue_0(False)
for _ in range(42):
    queue.enqueue(_)

print(f'Отфильтрованная очередь:{queue}')

