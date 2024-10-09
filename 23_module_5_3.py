class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'


    def __eq__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors == other.floors

    def __lt__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors < other.floors

    def __le__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors <= other.floors

    def __gt__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors > other.floors

    def __ge__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors >= other.floors

    def __ne__(self, other):
        if isinstance(other.floors, int) and isinstance(other, House):
            return self.floors != other.floors

    def __add__(self, value):
        if isinstance(value, int):
            self.floors = self.floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self


tb1 = House('Ленина, 35', 13)
tb2 = House('Губкина, 9', 10)

print(tb1)
print(tb2)

print(tb1 == tb2) # __eq__

tb2 = tb2 + 3 # __add__
print(tb2)
print(tb1 == tb2)

tb1 += 10 # __iadd__
print(tb1)

tb2 = 10 + tb2 # __radd__
print(tb2)

print(tb1 > tb2) # __gt__
print(tb1 >= tb2) # __ge__
print(tb1 < tb2) # __lt__
print(tb1 <= tb2) # __le__
print(tb1 != tb2) # __ne__