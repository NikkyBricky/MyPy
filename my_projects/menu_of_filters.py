
#  Фильтр - Азбука Морзе
def to_morse(text):
    abc_morse = {'а': '.-', 'б': '-...',  'в': '.--', 'г': '--.',  'д': '-..',   'е': '.',  'ж': '...-',
                 'з': '--..', 'и': '..', 'й': '.---',   'к': '-.-',  'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
                 'п': '.--.',  'р': '.-.',  'с': '...',   'т': '-',   'у': '..-',   'ф': '..-.',   'х': '....',
                 'ц': '-.-.', 'ч': '---.', 'ш': '----',  'щ': '--.-',   'ъ': '.--.-.',   'ы': '-.--',  'ь': '-..-',
                 'э': '..-..', 'ю': '..--', 'я': '.-.-',

                 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                 'y': '-.--', 'z': '--..',

                 '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                 '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                 ' ': ' ', '.': '......', ',': '.-.-.-', '?': '..--..', '!': '--..--'}
    for letter in text:
        if letter in abc_morse:
            letter = abc_morse[letter]
            print(letter, end='')
    print('\n')
#  ---------------------------------------------------------------------------------------------------------------------


# Фильтр червяка
def to_worm(text):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
              'a', 'e', 'i', 'o', 'u']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
                  'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь',

                  'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for letter in text:
        if letter in vowels:
            letter = '-'
        elif letter in consonants:
            letter = '_'
        print(letter, end='')
    print('\n')
#  ---------------------------------------------------------------------------------------------------------------------


# Фильтр картавости
def to_burr(text):
    for letter in text:
        if letter == 'р':
            letter = 'л'
        elif letter == 'к':
            letter = 'т'
        print(letter, end='')
    print('\n')
#  ---------------------------------------------------------------------------------------------------------------------


# Фильтр шепелявости
def to_lisp(text):
    for letter in text:
        if letter == 'с':
            letter = 'ш'
        if letter == 'з':
            letter = 'ж'
        if letter == 'т':
            letter = 'ч'
        if letter == 's' or letter == 'z':
            letter = 'th'
        print(letter, end='')
    print('\n')


# Фильтр рандомных цветов
def to_color(text):
    import random

    for letter in text:
        num_fore = random.randint(30, 37)
        num_back = random.randint(40, 47)
        if letter != ' ':
            print(f"\033[{num_fore}m{letter}", end='')
        else:
            print(f"\033[{num_back}m{letter}", end='')
        print("\033[0m", end='')
    print('\n')
#  ---------------------------------------------------------------------------------------------------------------------


# Фильтр рандомных букв
def to_random(text):
    import random

    alfbt = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
             'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
    alfbt_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    symbols = ['-', '_', '!', '?', '.', ',', ' ']

    ans = input('Вы хотите:\n'
                '1 - поменять буквы и пробелы\n'
                '2 - только буквы\n'
                '3 - только пробелы\n')
    while not(ans.isdigit() and 0 < int(ans) < 4):
        print('Нет такого ответа.')
        ans = input('Вы хотите:\n'
                    '1 - поменять буквы и пробелы\n'
                    '2 - только буквы\n'
                    '3 - только пробелы\n')
    ans = int(ans)
    print('Результат: ', end='')
    for letter in text:
        if letter in alfbt or letter in alfbt_en or letter in symbols:
            ran_letter = ''
            if letter in alfbt:
                ran_letter = random.choice(alfbt)
            elif letter in alfbt_en:
                ran_letter = random.choice(alfbt_en)
            ran_symbol = random.choice(symbols)
            if ans == 1:
                if letter != ' ':
                    letter = ran_letter
                else:
                    letter = ran_symbol
            if ans == 2:
                if letter != ' ':
                    letter = ran_letter
            if ans == 3:
                if letter == ' ':
                    letter = ran_symbol
        print(letter, end='')
    print('\n')
#  ---------------------------------------------------------------------------------------------------------------------


# Кричащий фильтр
def to_shout(text):
    print(text.upper() + '!!')
#  ---------------------------------------------------------------------------------------------------------------------


# Шепчущий фильтр
def to_whisper(text):
    print(text.lower() + '.')
#  ---------------------------------------------------------------------------------------------------------------------


# Фильтр из олимпиады по русскому языку
def to_strange_change(text):
    letters = {'а': 'я', 'б': 'п', 'в': 'б', 'г': 'в', 'д': 'г', 'е': 'э', 'ё': 'о',
               'ж': 'й', 'з': 'ж', 'и': 'ы', 'й': 'щ', 'к': 'г', 'л': 'л', 'м': 'м',
               'н': 'н', 'о': 'ё', 'п': 'б', 'р': 'р', 'с': 'з', 'т': 'д', 'у': 'ю',
               'ф': 'в', 'х': 'х', 'ц': 'й', 'ч': 'й', 'ш': 'й', 'щ': 'й', 'ы': 'и',
               'ь': '', 'ъ': '', 'э': 'е', 'ю': 'у', 'я': 'а'}
    for letter in text:
        if letter in letters:
            letter = letters[letter]
        print(letter, end='')
    print('\n')


#  Этап с меню записан в функции, чтобы его было удобно возвращать.
def choosing_filters():
    filters = {1: {'name': 'Morse filter',
                   'meaning': 'Преобразовывает все буквы в символы Азбуки Морзе '
                              '(Англ. яз., числа и знаки тоже поддерживаются).',
                   'function': to_morse},
               2: {'name': 'Worms filter',
                   'meaning': 'Преобразовывает все согласные в "_", а гласные в "-" (Англ. яз поддерживается).',
                   'function': to_worm},
               3: {'name': 'Burr filter',
                   'meaning': 'Преобразовывает букву "р" в "л", а букву "к" в "т" (картавость).',
                   'function': to_burr},
               4: {'name': 'lisp filter',
                   'meaning': 'Преобразовывает звуки "с", "з" и "т" в звуки "ш", "ж" и "ч" для русского языка,\n'
                              ' звуки "s" и "z" в звук "th" для английского языка (Шепелявить).',
                   'function': to_lisp},
               5: {'name': 'Random color',
                   'meaning': 'Окрашивает каждый символ текста в рандомный цвет.',
                   'function': to_color},
               6: {'name': 'Random change',
                   'meaning': 'Меняет каждую букву на рандомную, а пробел на рандомный символ '
                              '(Англ. яз поддерживается).',
                   'function': to_random},
               7: {'name': 'Shouting filter',
                   'meaning': 'Преобразовывает все буквы в заглавные и добавляет "!!" в конце.',
                   'function': to_shout},
               8: {'name': 'Whispering filter',
                   'meaning': 'Преобразовывает все буквы в строчные и добавляет "." в конце.',
                   'function': to_whisper},
               9: {'name': 'Strange_cipher filter',
                   'meaning': 'Меняет глухие парные согласные на звонкие,\n'
                              ' звонкие парные согласные'
                              ' на предшествующие им согласные в алфавите,\n'
                              ' все шипящие и "ц" на "й",\n'
                              ' все гласные на их "йотированные" пары'
                              '(напр. "а" на "я"),\n'
                              ' все сонорные согласные остаются теми же.\n'
                              ' (Шифр, подчиняющийся этим правилам, '
                              ' мне надо было разгадать на олимпиаде '
                              'по русскому языку)',
                   'function': to_strange_change},
               0: {'name': 'Выход'}}

    #  Задаем параметры меню
    len_bar = 4
    last_key = len(filters.keys()) - 1
    for num_key in range(0, len(filters.keys())):
        print(f'{num_key} - {filters[num_key]['name']}')

        #  Выводим меню с кол-вом строк, заданным в параметре len_bar (0 не считается)
        if num_key % len_bar == 0 and num_key != 0 and num_key != (last_key - 1):
            ans = input('Хотите увидеть еще (Да/Нет)?\n').lower()
            while ans != 'да' and ans != 'нет':
                print('Нет такого ответа.')
                ans = input('Хотите увидеть еще (Да/Нет)?\n').lower()
            if ans == 'нет':
                break

    chosen_filter = input('Выберите номер фильтра (или 0 для выхода):\n').lower()

    # Проверка ввода
    while not (chosen_filter.isdigit() and 0 <= int(chosen_filter) <= last_key):
        print('Нет такого фильтра.')
        chosen_filter = input('Выберите номер фильтра (или 0 для выхода):\n').lower()
    if int(chosen_filter) == 0:
        print('Удачи!')
        quit()

    # Вывод описания фильтра
    else:
        chosen_filter = int(chosen_filter)
        print(f'{filters[chosen_filter]['name']}: \n', filters[chosen_filter]['meaning'])
        print()

        choice = input('Хотите применить фильтр к тексту (Да/Нет)?\n').lower()

        while choice != 'да' and choice != 'нет':
            print('Нет такого ответа.')
            choice = input('Хотите применить фильтр к тексту (Да/Нет)?\n').lower()

        if choice == 'нет':
            choosing_filters()
        else:
            users_text = input('Введите текст, который хотите отфильтровать: ').lower()

            #  Вывод результата
            if chosen_filter != 6:  # так сделано, потому что слово "результат" выводится внутри функции для 6 фильтра
                print('Результат: ', end='')
            filters[chosen_filter]['function'](users_text)

            choosing_filters()


# Начало программы

choosing_filters()
