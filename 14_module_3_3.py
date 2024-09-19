# 1 Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(2, 3, 5)
print_params()
print_params(0)
print_params(c='apple', a=False, b=3)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2 Распаковка параметров
values_list = [False, 3.14, 'pine']
values_dict = {'a': 777, 'b': 'also', 'c': 99.99}
print_params(*values_list)
print_params(**values_dict)

# 3 Распаковка + отдельные параметры
values_list2 = [2, 'elt']
print_params(*values_list2, 42) # 42 встаёт на место параметра с функции