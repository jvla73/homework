# первая функция подсчитывает количество использований второй и третьей функций
# вторая функция возвращает информацию о строке-аргументе: длину, капс-вариант, вариант в нижнем регистре
# третья функция ищет заданное первым аргументом слово в списке, заданным вторым аргументом

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            so = True
            break
        else:
            so = False
    return so

print(string_info('cyclopentan'))
print(string_info('perhidrofenantren'))
print(string_info('year_plan'))
print(is_contains('turtle', ['Leo', 'Mike', 'Don', 'TurTle', 'Raph']))
print(is_contains('EARTH', ['Kuiper', 'Jupiter', 'Earth', 'Pluto', 'Sun']))
print(is_contains('peacH', ['banana', 'apple', 'watermelon']))
print(calls)