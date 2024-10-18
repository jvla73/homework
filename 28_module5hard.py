import time

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode: bool=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Новый пользователь {nickname} успешно зарегистрирован')

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            if not any(video.title == new_video.title for video in self.videos):
                self.videos.append(new_video)

    def get_videos(self, search_word: str):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title: str):
        if self.current_user is None:
            print('Войдите в аккаунт,чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
                for second in range(video.duration):
                    print(second, end=' ')
                    time.sleep(1)
                video.time_now = 0
                print('Конец видео')
                return

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Язык программирования C++', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Язык программирования C++')
ur.register('jvla73', 'l0lk3k43bUr3k', 13)
ur.watch_video('Язык программирования C++')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Язык программирования C++')

# Проверка входа в другой аккаунт
ur.register('jvla73', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')