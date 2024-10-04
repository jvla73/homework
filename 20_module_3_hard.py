# функция считает количество всех элементов всех переданных последовательностей,
# число принимает за число, строку складывает по len() строки (кол-во символов)

def calculate_structure_sum(data_structure):
    sum_numbers = 0
    sum_strings = 0

    def recurse(data):
        nonlocal sum_numbers, sum_strings
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                recurse(item)
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        elif isinstance(data, int) or isinstance(data, str):
            if isinstance(data, int):
                sum_numbers += data
            elif isinstance(data, str):
                sum_strings += len(data)

    recurse(data_structure)
    return sum_numbers + sum_strings

print(calculate_structure_sum(
    [                                           # передать список, содержащий
        [1, 2, 3],                              # список,
        {'a': 4, 'b': 5},                       # словарь,
        (
            6,                                  # кортеж с числом 6 и словарём,
            {'cube': 7, 'drum': 8}
        ),
        "Hello",                                # строку,
        (                                       # кортеж, содержащий
            (),                                 # пустой кортеж и
                [                               # список, содержащий
                    {                           # множество, содержащее
                        (                       # кортеж, содержащий
                            2, 'Urban',         # число, строку
                            ('Urban2', 35)      # и кортеж со строкой и числом
                        )
                    }
                ]
        )
    ]
))