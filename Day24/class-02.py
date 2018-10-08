class Person:
    def __int__(self, n, a, g, f):
        self.name = n
        self.age = a
        self.gendaer = g
        self.fight = g


role_list = []

y_n = input("Do you want create roles")
if y_n == "y":
    name = input("name")
    age = input("age")
    role_list.append(Person())

role_list[1]