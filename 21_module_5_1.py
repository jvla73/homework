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

tower_block = House('tower-block', 13)
semidetached = House('semidetached', 2)
villa = House('villa', 4)

tower_block.go_to(9)
print()
semidetached.go_to(3)
print()
villa.go_to(3)
