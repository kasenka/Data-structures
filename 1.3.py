 # Создайте класс «Студент» с атрибутами имя, возраст и список оценок.
 # Напишите методы для вычисления среднего балла и определения успеваемости студента (средний балл выше 4).
 # Используйте магический ме-тод __repr__ для вывода информации о студенте в виде «Студент {имя}, возраст {возраст}».

class Student:
    def __init__(self, name, age, marks):
        self.age = age
        self.name = name
        self.marks = marks

    def sr_ball(self):
        ball = sum(self.marks) / len(self.marks)
        return ball

    def is_successful(self):
        return self.sr_ball() > 4.0


    def __repr__(self):
        return f'Студент {self.name}, возраст {self.age}'

student = Student("Иван", 20, [5, 4, 3, 5, 4])

print(student)
print(f'Средний балл: {student.sr_ball()}')
print(f'Успеваемость: {"успешен" if student.is_successful() else "не успешен"}')