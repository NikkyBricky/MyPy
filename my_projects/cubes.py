import random
import time
i = 0
print('Привет,давай сыграем в игру "кубик"')
answer_pers = input('Введи число от 1 до 6:\n')
if answer_pers.isdigit():
    answer_pers = int(answer_pers)
    if answer_pers < 1 or answer_pers > 6:
        print('Неверное число. Попробуй снова')
    else:
        answer_bot = random.randint(1, 6)
        print('Бросаем кубик', end='')
        time.sleep(0.7)
        while i < 3:
            print('.', end='')
            time.sleep(0.7)
            i += 1
        print('')
        if answer_pers == answer_bot:
            print('Правильно! Ты молодец!')
        else:
            print('Неа! Попробуй еще раз.')

else:
    print('Кажется, ты ввел что-то не то..')
