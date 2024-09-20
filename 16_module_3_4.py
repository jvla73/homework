# функция принимает слово/корень и кортеж слов, в кортеже находит
# однокоренные слову/корню

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('able', 'Able', 'Mable', 'Disable', 'Bagel', 'Disablement')
result4 = single_root_words('ana', 'anagram', 'bAnAnA', 'anomalous', 'Anna')
result5 = single_root_words('лог', 'логарифм', 'КаТаЛоГ', 'ЛОЖКА', 'иней', 'арбуз')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)