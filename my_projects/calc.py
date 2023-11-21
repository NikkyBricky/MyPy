import math
x = input('Введи первое число: ')
try:
    float(x)
    is_dig = True
except ValueError:
    is_dig = False
if is_dig:
    x = float(x)
    operator = input('Какую операцию ты хочешь выполнить?(*, /, +, -, %, **, корень)\n Можешь написать словами:\n')
    operator = operator.lower()
    if  operator == "*" or operator == '/' or operator == '+' or operator == '-' or operator == '%' or operator == '**':
        y = input('Введи второе число: ')
        try:
            float(x)
            is_dig = True
        except ValueError:
            is_dig = False
        if is_dig:
            y = float(y)
            if operator == "*" or operator == 'умножение':
               print(x * y)
            if operator == '/' or operator == 'деление':
                if y == 0:
                    print('Ошибка. На ноль делить нельзя.')
                else:
                    print(x / y)
            if operator == '+' or operator == 'сложение':
                print(x + y)
            if operator == '-' or operator == 'вычитание':
                print(x - y)
            if operator == '%' or operator == 'остаток':
                print(x % y)
            if operator == '**':
                print(x**y)
        else:
            print(f'{y} не является числом.')
    elif operator == 'корень':
        if x < 0:
            print('Корень можно извлекать только из неотрицательных чисел.')
        else:
            print(f'Корень 2 степени из числа {x} = {math.sqrt(x)}')
    else:
       print('Команда введена неверно.')
else:
    print(f'{x} не является числом.')