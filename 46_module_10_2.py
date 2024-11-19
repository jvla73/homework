from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        enemies = 100
        while enemies > 0: # >= self.power
            sleep(1)
            days += 1
            enemies = enemies - self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {days}-й день, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

threads = []

knight1 = Knight('Ланселот', 10)
knight2 = Knight('Артур', 20)
knight1.start()
knight2.start()

threads.append(knight1)
threads.append(knight2)

for thread in threads:
    thread.join()
print('Все битвы закончились!')