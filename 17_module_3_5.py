# функция принимает целое число и подсчитывает произведение цифр этого числа

def get_multiplied_digits(number):
    str_number = str(number)                                        # преобразуем число в строку,
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))   # чтобы при преобразовании строки в число
    else:                                                           # убирать первые нули
        return first

result1 = get_multiplied_digits(40203)      # 24
print(result1)
result2 = get_multiplied_digits(1001001)    # 1
print(result2)
result3 = get_multiplied_digits(5820)       # 0 – в конце всё умножается на 0
print(result3)
result4 = get_multiplied_digits(5082)       # 80
print(result4)
result5 = get_multiplied_digits(20572)      # 140
print(result5)
result6 = get_multiplied_digits(25)         # 10
print(result6)