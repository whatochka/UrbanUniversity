import hashlib
import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def __str__(self):
        return f"Пользователь {self.nickname}, {self.age} лет."

    @staticmethod
    def hash_password(password: str):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)


class Video:
    def __init__(self, title: str, duration: float, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Видео {self.title}, {self.duration} секунд"

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()


class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} существует")
            return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if not any(existing_video == video for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_query: str):
        search_query = search_query.lower()
        return [video.title for video in self.videos if search_query in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return

                print(f"Воспроизведение видео: {video.title}")
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end="   ")
                    time.sleep(1)
                print("\nКонец видео")
                video.time_now = 0
                return

        print(f"Видео {title} не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
