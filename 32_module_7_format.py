# форматирование строк
# описание команд Мастера кода и Волшебники данных

# команды, форматирование через %
team1_num = int(input('Введите количество участников первой команды: '))
team2_num = int(input('Введите количество участников второй команды: '))
print('В команде Мастера кода %s участников.' % team1_num)
print('В команде Волшебники данных %s.' % team2_num)

# решенные задачи и время, *.format
score_1 = int(input('Введите количество решённых первой командой задач: '))
score_2 = int(input('Введите количество решённых второй командой задач: '))
print('Команда Мастера кода решила {} задач.'.format(score_1))
print('Команда Волшебники данных решила {} задач.'.format(score_2))
team1_time = float(input('Введите время решённых первой командой задач в секундах: '))
team2_time = float(input('Введите время решённых второй командой задач в секундах: '))
print('Мастера кода решили задачи за {} сек.'.format(team1_time))
print('Волшебники данных решили задачи за {} сек.'.format(team2_time))

# итоги игры, f-строки
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / 2

print(f'Всего команды решили:\nМастера кода: {score_1} задач\nВолшебники данных: {score_2} задач\n'
      f'Время решения задач по командам:\nМастера кода: {team1_time}\nВолшебники данных: {team2_time}')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result =  'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(challenge_result)
print(f'Всего решено задач: {tasks_total}\nСреднее время решения: {time_avg}')