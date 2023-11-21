import math
a = int(input('Введи коэф. a:'))
b = int(input('Введи коэф. b:'))
c = int(input('Введи коэф. c:'))
x = 0
D = b**2 - 4*a*c
if D < 0:
    print('Нет решений')
if D > 0:
    x1 = (-b + math.sqrt(D))/2*a
    x2 = (-b - math.sqrt(D))/2*a
    print(x1, x2)
if D == 0:
    x0 = (-b)/2*a
    print(x0)
