
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, data):
        if self.head is None:
            return
        elif self.head.data == data:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is None:
                return
            else:
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def sort_list(self):
        current = self.head
        sort_l = []
        while current:
            sort_l.append(current.data)
            current = current.next
        sort_l.sort(key=len)
        return sort_l

    def __str__(self):
        lt = self.sort_list()
        if lt == None:
            return f"Двусвязный список пустой"
        dllist_str = ""
        for i in range(len(lt)):
            dllist_str += " ⇄ " + str(lt[i])

        return dllist_str.lstrip(" ⇄ ")

#Реализовать функцию, которая объединяет два отсортированных двусвязных списка в один отсортированный список.

step1 = [1,2,3]
step2 = ['23',4,'5','67',7]

step3 = [34,'122','5',1,1,1]
step4 = []
step5 = ['4']

numbers = DoublyLinkedList()
for i in range(1,3):
    numbers.add_node(globals()[f"step{i}"])

numbers_2 = DoublyLinkedList()
for i in range(3,6):
    numbers_2.add_node(globals()[f"step{i}"])

# print(numbers_2)
# print(numbers)

def list_join(list_1,list_2):
    new = list_1 + list_2
    sum_list = DoublyLinkedList()
    for i in new:
        sum_list.add_node(i)
    return sum_list

print(list_join(numbers.sort_list(),numbers_2.sort_list()))
