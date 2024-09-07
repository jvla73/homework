# словари, множества и списки

# решение с пустым словарём
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average = {} # пустой словарь
students = sorted(students) # упорядочили + создали список
# наполняем пустой словарь
average.update({students[0]: sum(grades[0]) / len(grades[0])})
average.update({students[1]: sum(grades[1]) / len(grades[1])})
average.update({students[2]: sum(grades[2]) / len(grades[2])})
average.update({students[3]: sum(grades[3]) / len(grades[3])})
average.update({students[4]: sum(grades[4]) / len(grades[4])})
# выводим пустой словарь в терминал
print(average)

# первое моё решение, не соответствует условию про пустой словарь
#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#students = sorted(students) # упорядочили + создали список
#average = dict([[students[0], sum(grades[0]) / len(grades[0])],
#                [students[1], sum(grades[1]) / len(grades[1])],
#                [students[2], sum(grades[2]) / len(grades[2])],
#                [students[3], sum(grades[3]) / len(grades[3])],
#                [students[4], sum(grades[4]) / len(grades[4])]])
#print(average)
