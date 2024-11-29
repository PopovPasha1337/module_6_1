import time
import hashlib
from re import search


class User:
    def __init__(self,nickname, password, age ):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode(). hexdigest())
        self.age = age
class Video:
    def __init__(self, title, duration, time_now=0, abult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = abult_mode
class Urtube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = []
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                return
        print(f'Пользователь{nickname}не найден')
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Пользователь {nickname} уже существуте')
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
    def get_videos(self, search_word):
        return [v.title for v in self.videos if search_word.lower() in v.title.lower()]
    def watch_videos(self, title):
        for video in self.videos:
            if video.title == title:
                if self.current_user in None:
                    print('Войдите в аккаунт. чтобы смотреть видео')
                    return
                if self.current_user.age < 18 and video.adult_mode:
                    print('Вам не 18 летб пожалуйста покиньте страницу')
                    return
                while video.time_now < video.duration:
                    print(video.time_now)
                    video.time_now += 1
                    time.sleep(1)
                    print('Конец видое')
                    video.time_now = 0
                    return
                print(f'Видео {title} не найдено')
                ur = Urtube
                v1 = Video('Лучший язык программирования 2024 года', 200)
                v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
                ur.add(v1, v2)
                print(ur.get_videos('лучший'))
                print(ur.get_videos('ПРОГ'))
                ur.watch_videos('Для чего девушкам парень программист?')
                ur.register('vasya_pupkin', 'lolkekcheburek', 13)
                ur.watch_videos('Для чего девушкам парень программист')
                ur.register('urban_pythonist', 'hbgheagilheagh', 55)
                ur.watch_videos('Как сделать вывод в питоне')
                ur.register('vasya_pupkin', 'egrerhghe', 55)
                ur.watch_videos('Лучший язык в программирования 2024 года(конечно python и обучайтесь в Urbane)')




