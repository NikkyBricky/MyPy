from PIL import Image
import requests


def check_ans(text):
    while not (text.isdigit() and int(text) in range(101)):
        print('Такого значения параметра нет. Пожалуйста, введите число от 0 до 100.')
        text = input('Введите параметр:\n')
    return text


def parameters():
    global lim_value_clean, lim_value_dirt, lim_danger
    lim_value_clean = input('Введите пороговое значение доли ценного элемента в чистом образце,'
                            'выше которого извлекать его выгодно:\n')
    lim_value_clean = check_ans(lim_value_clean)
    lim_value_dirt = input('Введите пороговое значение доли ценного элемента грязном образце,'
                           'выше которого извлекать его выгодно:\n')
    lim_value_dirt = check_ans(lim_value_dirt)
    lim_danger = input('Введите пороговое значение радиоактивных примесей, делающее образец опасным:\n')
    lim_danger = check_ans(lim_danger)


lim_value_clean = ''
lim_value_dirt = ''
lim_danger = ''
parameters()
while True:
    def trying_url():
        while True:
            print()
            url1 = input('Введите:\n'
                         'Ссылку на минерал\n'
                         '1 - изменить параметры\n'
                         '0 - для выхода\n')
            if url1 == '0':
                quit('Удачи!')
            if url1 == '1':
                parameters()
            #  noinspection PyBroadException
            try:
                requests.get(url1)

            except Exception:
                if url1 != '1':
                    print('Кажется, ссылка введена неверно.')
            else:
                return url1


    url = trying_url()
    mineral = Image.open(requests.get(url, stream=True).raw).convert('L')
    w, h = mineral.size
    all_ore = w * h
    count_val = 0
    count_dang = 0
    for i in range(w):
        for j in range(h):
            color = mineral.getpixel((i, j))
            if color <= 42:
                count_val += 1
            if color > 210:
                count_dang += 1

    per_value = count_val / all_ore * 100
    per_danger = count_dang / all_ore * 100
    print('Ответ робота:')
    if per_danger < int(lim_danger) and per_value < int(lim_value_clean):
        print('И ради такого меня посылали? Спасибо, не надо. Отправлю это в отвал!')
    elif per_danger < int(lim_danger):
        print('А вы спрашиваете, ради чего я корячусь тут… Ради такого! Отвезу в чистый цех!')
    if per_danger >= int(lim_danger) and per_value >= int(lim_value_dirt):
        print('В этом что-то есть. Дам ему шанс в грязном цехе!')
    elif per_danger >= int(lim_danger):
        print('В этом что-то есть. Но мне здоровье дороже. Отвезу-ка в могильник!')
