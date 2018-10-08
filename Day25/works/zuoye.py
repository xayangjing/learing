class Teacher:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary


class Course:
    def __init__(self, name, cost, teacher):
        self.name = name
        self.teacher = teacher
        self.cost = cost

    def class_up(self):
        self.teacher.salary += self.cost


t1 = Teacher('John', 32,1000)

c1 = Course('Powershell', 1, t1)

print(c1.teacher.salary)
print(c1.name)
print(c1.teacher.name)
c1.class_up()
print(c1.teacher.salary)


