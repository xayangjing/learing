# class Province:
#     country = 'China'
#
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#
#
# print(Province.country)
#
# hebei = Province("He bei")
# print(hebei.name)
# print(hebei.country)


class Father:

    def nanqiu(selfs):
        pass

    def zuqiu(self):
        pass

    def chouyan(self):
        pass

    def hejiu(self):
        pass

    def tangtou(self):
        pass


class Son(Father):

    def baojian(self):
        pass


class Base:
    def a(self):
        print("Base")


class F0(Base):
    def a1(self):
        print('F0.a')


class F1(F0):
    def a1(self):
        print('F1.a')


class F2:
    def a1(self):
        print('F2.a')


class s(F1, F2):
    pass


obj = s()
obj.a()
