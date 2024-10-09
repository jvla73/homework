class House:

    houses_history = [] # хранит название созданных объектов

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')

tb1 = House('Ленина, 35', 13)
print(House.houses_history)
tb2 = House('Губкина, 9', 10)
print(House.houses_history)
tb3 = House('Свердлова, 5', 11)

del tb1
del tb2

print(House.houses_history)