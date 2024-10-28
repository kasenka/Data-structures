
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

        self.name = self.data['name']
        self.price = self.data['price']
        self.amount = self.data['amount']
        self.date_of_buying = self.data['date_of_buying']

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

    def __str__(self):
        if self.head == None:
            return f"Двусвязный список пустой"
        current = self.head
        dllist_str = ""
        while current:
            dllist_str += '\n' + str(current.data) +" ⇄ "
            current = current.next
        return dllist_str.lstrip(" ⇄ ")

#Создайте двусвязный список для хранения информации о покупках в интернетмагазине.
# Каждый элемент списка должен содержать название товара, цену, количество и дату покупки.

purchase = DoublyLinkedList()

good_1 = {'name': 'Сыр',
          'price': 600,
          'amount': 0.25 ,
          'date_of_buying': '04.04.2024' }
good_2 = {'name': 'Честер_вишневый',
          'price': 95,
          'amount': 3,
          'date_of_buying': '30.03.2024' }
good_3 = {'name': 'Добрый_кола',
          'price': 88,
          'amount': 1,
          'date_of_buying': '03.04.2024' }
good_4 = {'name': 'Mac&Cheese',
          'price': 350,
          'amount': 1,
          'date_of_buying': '17.01.2024' }

for i in range(1,5):
    purchase.add_node(globals()[f"good_{i}"])

print(purchase)
