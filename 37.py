class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    def delete(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node == self.head:
                    self.head = current_node.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def go_end(self, amount):
        for i in range(amount):
            current_node = self.head
            self.append(current_node.data)
            self.delete(current_node.data)

    def __str__(self):
        cdllist_str = ""
        current_node = self.head
        while current_node:
            cdllist_str += str(current_node.data) + " ⇄ "
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ⇄ " + cdllist_str

# Реализовать функцию, которая перемещает заданное количество элементов из начала циклического двусвязного списка в его конец.

step1 = []
step2 = ['4']
step3 = [1,2,3]
step4 = ['23',4,'5','67',7]
step5 = [34,'122','5',1,1,1]


numbers = CircularDoublyLinkedList()
for i in range(1,6):
    numbers.append(globals()[f"step{i}"])

numbers.go_end(4)
print(numbers)



