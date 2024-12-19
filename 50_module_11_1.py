import requests

# запрос GET с настроенными заголовками
headers = {'User-Agent': 'MyUserAgent/1.0'}
response = requests.get('https://www.example.com', headers=headers)
print(response.status_code)

# запрос POST с данными формы
data = {'username': 'admin', 'password': 'secret'}
response = requests.post('https://www.example.com/login', data=data)
print(response.text)  # Выводит текст ответа

# использование сессии
session = requests.Session()
session.auth = ('user', 'pass')  # Указывает учетные данные аутентификации
response = session.get('https://www.example.com/protected')
print(response.text)  # Выводит текст защищенной страницы

# использование прокси-сервера
proxy = {'http': 'http://127.0.0.1:8080'}
response = requests.get('https://www.example.com', proxies=proxy)
print(response.status_code)

# загрузка файла
response = requests.get('https://www.example.com/image.jpg')
with open('image.jpg', 'wb') as f:
    f.write(response.content)  # Сохраняет изображение в файл

# обработка ошибок и повторное подключение
try:
    response = requests.get('https://www.example.com/non-existing-page')
    response.raise_for_status()  # Вызовет исключение, если статус-код не 2xx
except requests.exceptions.HTTPError as e:
    print(e)
    # Повторно выполните запрос с повышенным значением таймаута
    response = requests.get('https://www.example.com/non-existing-page', timeout=10)

# настраиваемый таймаут
timeout = (5, 10)  # Указывает таймаут подключения и чтения
response = requests.get('https://www.example.com', timeout=timeout)
print(response.status_code)