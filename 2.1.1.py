
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item

    def __str__(self):
        current_item = self.head
        s = ''
        while current_item:
            s += str(current_item.data) + ' '
            current_item = current_item.next
        return s

# Дан стек. Необходимо удалить из него все элементы, которые не являются делителями последнего элемента стека.

stack = Stack()

for i in range(15,0,-1):
    stack.push(i)

print(stack)

def func(stack):
    sp = []
    while not stack.is_empty():
        sp.append(stack.pop())
    for item in [i for i in sp if i > 0 and (sp[-1] % i) == 0]:
        stack.push(item)
    return stack

print(func(stack))
