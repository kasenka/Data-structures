#Создать класс очереди, который будет хранить только элементы типа int и отсортированные по убыванию.
# При добавлении элемента, если он не является целым числом, то он не должен добавляться.
# При получении элементов из очереди они должны быть отсортированы по убыванию.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not (self.head is None and self.tail is None)

    def queue_data(self):
        current = self.head
        s = []
        while current:
            s.append(current.data)
            current = current.next
        return s

    def push(self, data):
        if isinstance(data, int):
            if data not in self.queue_data():
                new_node = Node(data)
                if not self.head:
                    self.head = new_node
                else:
                    if data >= self.head.data:
                        new_node.next = self.head
                        self.head = new_node
                    else:
                        current = self.head
                        while current.next is not None and data < current.next.data:
                            current = current.next
                        new_node.next = current.next
                        current.next = new_node
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def __str__(self):
        current = self.head
        s = ''
        while current:
            s += str(current.data) + ' '
            current = current.next
        return s

queue = Queue()

# # for i in range(15,0,-1):
# #     queue.push(i)
queue.push(1)
queue.push(13)
queue.push(2.0)
queue.push(5)
queue.push(4)
queue.push(4)
queue.push(1)
#
#
print(queue)

#Создать класс очереди, который будет хранить только уникальные элементы.
# При добавлении элемента, если он уже есть в очереди, то он не должен добавляться.