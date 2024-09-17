def send_email (message, recipient, sender='university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not recipient.endswith('com') and not recipient.endswith('ru') and not recipient.endswith('net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not sender.endswith('com') and not sender.endswith('ru') and not sender.endswith('net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'jvla73@gmail.com')
send_email('Задание проверено!', 'jvla73@gmail.com', sender='noreply@members.tildacdn.com')
send_email('Задание исправлено!', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Следующий вебинар 23го сентября', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')