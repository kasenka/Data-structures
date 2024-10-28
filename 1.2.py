# Создайте класс ПРОДУКТ с методами, позволяющими вывести на экран информацию о продукте,
# а также определить, подходит ли данный продукт для заданных условий.
# Создайте дочерние классы МЯСО (название, цена, производитель, срок годности),
# ОВОЩИ (название, цена, производитель, сезонность),
# ФРУКТЫ (название, цена, производитель, сезонность) со своими методами вывода информации на экран и определения
# соответствия заданным условиям. Создайте список продуктов, выведите полную информацию из базы на экран,
# а также организуйте поиск продуктов с заданной ценой или сезонностью.

class Good:
    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        self.owner = owner

    def get(self):
        print(f'название - {self.name}')
        print(f'цена - {self.price}')
        print(f'производитель - {self.owner}')

    def is_match(self, price = None, season = None):
        if price:
            return self.price == price
        if season:
            return self.season == season

class Meat(Good):
    def __init__(self,name, price, owner, srok):
        super().__init__(name, price, owner)
        self.srok = srok

    def get(self):
        super().get()
        print(f'срок годности - {self.srok}')

    def is_match(self, price = None, season = None):
         return super().is_match(price)

class Vegetables(Good):
    def __init__(self, name, price, owner, season):
        super().__init__(name, price, owner)
        self.season = season

    def get(self):
        super().get()
        print(f'сезонность - {self.season}')

    def is_match(self, price = None, season = None):
        return super().is_match(price, season)

class Fruts(Good):
    def __init__(self, name, price, owner, season):
        super().__init__(name, price, owner)
        self.season = season

    def get(self):
        super().get()
        print(f'сезонность - {self.season}')

    def is_match(self, price = None, season = None):
        return super().is_match(price, season)

g = Good('s',123,'d')

meat = Meat('pork', 111, 'smb', 14)
vegetables = Vegetables('potato',34,'sbd','summer')
fruts = [Fruts('mango',394,'sbd','summer'),
         Fruts('mangro',3914,'sbd','no'),
         Fruts('maerngo',3094,'sbd','summer'),
         Fruts('ma34ngo',34,'sbd','no'),]

# print(meat.is_match(111))
# meat.get()
#
# print(vegetables.is_match(season= 'summer'))
# vegetables.get()

for frut in fruts:
    if frut.is_match(season= 'summer'):
        frut.get()
