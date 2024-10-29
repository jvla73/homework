def custom_write(file_name, strings):
    str_pos = {}
    str_num = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        by_pos = file.tell()
        str_num += 1
        file.write(string + '\n')
        str_pos[(str_num, by_pos)] = string
    return str_pos

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)