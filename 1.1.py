# Опишите класс Student, заданный фамилией, именем, возрастом и сред-ним баллом.
# Включите в описание класса методы: вывода информации о студенте на экран, проверки, является ли студент отличником
# (средний балл больше 4.5), и свойство, позволяющее установить факультет, на котором учится студент.

class Student:
    def __init__(self, surname, name, age, mid_mark):
        self.surname = surname
        self.name = name
        self.age = age
        self.mid_mark = mid_mark
        self.fackultet = None

    def get(self):
        return f'фамилией - {self.surname}, именем - {self.name}, возрастом - {self.age} и сред-ним баллом - {self.mid_mark}'

    def is_otlich(self):
        return 'Отличник' if self.mid_mark > 4.5 else 'Не отличник'

student = Student('Kosenko', 'Dasha', 18, 4.8)

print(student.get())

print(student.is_otlich())

student.fackultet = 'itiabd'
