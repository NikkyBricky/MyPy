# импорты
import random
import time


def cef():
    # пол пользователя
    ending = 'ам'
    gender = input('Твой пол:\n').lower()
    while (gender != 'мужской' and gender != 'муж' and gender != 'м' and
           gender != 'женский' and gender != 'жен' and gender != 'ж'):
        print('Пол введен неверно.')
        gender = input('Твой пол:\n')
    if gender == 'мужской' or gender == 'муж' or gender == 'м':
        ending = ''
    elif gender == 'женский' or gender == 'жен' or gender == 'ж':
        ending = 'а'

    # ответ пользователя
    answer_pers = input('камень, ножницы или бумага?\n').lower()
    while answer_pers != 'камень' and answer_pers != 'ножницы' and answer_pers != 'бумага':
        print(f'кажется, ты ввел{ending} что-то не то.. Попробуй снова.')
        answer_pers = input('камень, ножницы или бумага?\n').lower()

    # создание ответов для робота и проверка ответа пользователя
    answers = ['камень', 'ножницы', 'бумага']
    answer_bot = random.choice(answers)

    # вывод считалочки
    print('камень, ', end='')
    time.sleep(0.4)
    print('ножницы, ', end='')
    time.sleep(0.4)
    print('бумага, ', end='')
    time.sleep(0.4)
    print('раз, ', end='')
    time.sleep(0.4)
    print('два, ', end='')
    time.sleep(0.4)
    print('три')
    # --------------------------------

    # вывод результата
    print(f'Твой ответ: {answer_pers}')
    print(f'Ответ робота: {answer_bot}')
    if answer_pers == 'камень':
        if answer_bot == 'камень':
            print('Ничья')
        if answer_bot == 'бумага':
            print(f'Ты проиграл{ending}.')
        if answer_bot == 'ножницы':
            print(f'Ты выиграл{ending}!')
    if answer_pers == 'ножницы':
        if answer_bot == 'ножницы':
            print('Ничья')
        if answer_bot == 'камень':
            print(f'Ты проиграл{ending}.')
        if answer_bot == 'бумага':
            print(f'Ты выиграл{ending}!')
    if answer_pers == 'бумага':
        if answer_bot == 'бумага':
            print('Ничья')
        if answer_bot == 'ножницы':
            print(f'Ты проиграл{ending}.')
        if answer_bot == 'камень':
            print(f'Ты выиграл{ending}!')
    print()
    print()
    cef()


cef()
