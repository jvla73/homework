import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = __file__
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(__file__)
        parent_dir = os.path.dirname(__file__)

print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')