# программа подбирает пары чисел, сумме которых кратно введённое число
# в диапазоне от 1 до этого числа

n = int(input('Введите ключ: '))

pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''

for i in pairnum1:
    for j in pairnum2:
        pair1 = i
        pair2 = j
        if pair1 >= pair2:
            continue
        else:
            aliquot = n % (pair1 + pair2)
            if aliquot == 0:
                pairs.append([pair1, pair2])
                result = result + str(pair1) + str(pair2)
print('Пары чисел', *pairs)
print('Пароль:', result)