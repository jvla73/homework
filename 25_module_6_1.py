# классы Animal и Plant имеют подклассы Mammal и Predator, Flower и Fruit;
# описано их взаимодействие и некоторые его последствия

class Animal # звери
    def __init__(self, name)
        self.name = name
        self.alive = True
        self.fed = False

class Mammal(Animal) # млекопитающие
    def eat(self, food) # млекопит может есть фрукты, но не ест цветы
        if food.edible
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else
            print(f'{self.name} не может съесть {food.name}')
            self.alive = False
            print(f'{self.name} умер')

class Predator(Animal) # хищные
    def eat(self, food) # хищник не может есть растения
        if isinstance(food, Plant)
            print(f'{self.name} не может съесть {food.name}')
            self.alive = False
            print(f'{self.name} умер')
        else
            self.fed = True
            print(f'{self.name} съел {food.name}')

class Plant # растения просто есть, их едят или нет
    def __init__(self, name)
        self.name = name
        self.edible = False

class Flower(Plant) # цветки не едят
    def __init__(self, name)
        super().__init__(name)
        self.edible = False

class Fruit(Plant) # фрукты едят
    def __init__(self, name)
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)