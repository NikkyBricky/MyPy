films = {}
film_name = None


def check_rate(f_rate):
    while not (f_rate.isdigit() and 0 <= int(f_rate) <= 5):
        print('Введена неверная оценка.')
        f_rate = input('Введи оценку от 0 до 5:\n')
    return f_rate


while True:
    film_name = input('Введи название фильма или напиши "q" для продолжения:\n').lower()
    if film_name == 'q':
        break
    film_rate = input('Оцени фильм от 0 до 5:\n')
    film_rate = check_rate(film_rate)
    films[film_name] = film_rate
ask_film = input('Какой фильм ты хочешь найти?\n').lower()
while ask_film not in films:
    print('Нет такого фильма.')
    ask_film = input('Какой фильм ты хочешь найти?\n').lower()
print(f'Фильм "{ask_film}" имеет оценку {films[ask_film]}.')
while True:
    min_rate = input('Введи минимальную оценку от 0 до 5 или q для выхода:\n').lower()
    if min_rate == 'q':
        quit()
    min_rate = check_rate(min_rate)
    print(f'Фильмы, имеющие оценку не ниже {min_rate}: ')
    for name, rate in films.items():
        if films[name] >= min_rate:
            print(f'Фильм "{name}" имеет оценку {rate}.')
