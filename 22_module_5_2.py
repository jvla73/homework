class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


tower_block = House('Многоэтажка', 13)
semidetached = House('Дом для двух семей', 2)
villa = House('Вилла', 4)

# tower_block.go_to(9)
# print()
# semidetached.go_to(3)
# print()
# villa.go_to(3)
# print()
print(tower_block)
print(semidetached)
print(villa)
print()
print(len(tower_block))
print(len(semidetached))
print(len(villa))
