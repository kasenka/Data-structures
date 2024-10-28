class Stack_0:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)




class Node:
    def __init__(self, data):
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

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self.head
        stack_str = ""
        while current:
            stack_str += str(current.data) + ' '
            current = current.next
        return stack_str


# Дан стек. Необходимо удалить из него все элементы, которые не являются простыми числами.
def pros(data):
    check_data = [i for i in range(2, int((data) ** 0.5) + 1) if data % i == 0]
    return not check_data

# def filt(stack):
#     stack_prom = stack
#     for _ in range(stack.size()):  # фильтруем 1 стек и заполняем промежуточный
#         el = stack.pop()
#         if pros(el):
#             stack_prom.push(el)
#
#     stack_filt = Stack_0()
#     for _ in range(stack_prom.size()):
#         el = stack_prom.pop()
#         stack_filt.push(el)
#
#     return print(f'Стек_2: {stack_filt}')



stack = Stack()
for i in range(42, 0, -1):  # заполняем стек
    stack.push(i)

# filt(stack)
print(f'Стек_1: {stack}')


stack_prom = Stack()
for _ in range(stack.size()):  # фильтруем 1 стек и заполняем промежуточный
    el = stack.pop()
    if pros(el):
        stack_prom.push(el)

stack_filt = Stack()
for _ in range (stack_prom.size()):
    el = stack_prom.pop()
    stack_filt.push(el)


print(f'Стек_2: {stack_filt}')

