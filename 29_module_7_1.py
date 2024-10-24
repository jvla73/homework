class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        product = f'{self.name}, {self.weight}, {self.category}'
        return product

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        str_prod = file.read()
        file.close()
        return str_prod

    def add(self, *products):
        getter = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if getter.find(f'{i.name}') == -1:
                file.write(f'{i}\n')
            else:
                print(f'Продукт {i.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 5.5, 'Vegetables')
p2 = Product('Pasta', 0.2, 'Groceries')
p3 = Product('Apples', 1.5, 'Fruits')
p4 = Product('Avocado', 2.0, 'Fruits')

s1.add(p1, p2, p3, p4)
print() # пустая строка, чтобы отделить выводы друг от друга
print(s1.get_products())
