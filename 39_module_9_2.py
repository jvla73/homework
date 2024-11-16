first_strings = ['Cait', 'Violet', 'Grayson', 'Ekko', 'Amara']
second_strings = ['Jinx', 'Vander', 'Medarda', 'Isha', 'Silco']

first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

allin = first_strings + second_strings
third_result = {x: len(x) for x in allin if len(x) % 2 == 0}
print(third_result)