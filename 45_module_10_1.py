import time
from time import sleep
from threading import Thread

time_start = time.time()

def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = time.time()
print(f'Работа потоков {time_end - time_start}')

time_start = time.time()

thread_a = Thread(target=write_words, args=(10, 'example5.txt'))
thread_b = Thread(target=write_words, args=(30, 'example6.txt'))
thread_c = Thread(target=write_words, args=(200, 'example7.txt'))
thread_d = Thread(target=write_words, args=(100, 'example8.txt'))

thread_a.start()
thread_b.start()
thread_c.start()
thread_d.start()

thread_a.join()
thread_b.join()
thread_c.join()
thread_d.join()

time_end = time.time()
print(f'Работа потоков {time_end - time_start}')