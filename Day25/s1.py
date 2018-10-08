'''
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()


v = None

while True:
    if v:
        v.show()
    else:
        v = Foo('alex', 123)
        v.show()
'''

'''
class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v


obj = Foo.get_instance()

obj2 = Foo.get_instance()
print(obj)
print(obj2)
'''

