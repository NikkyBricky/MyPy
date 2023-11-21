user_name = input('Представься:\n').lower()
all_names = [None]
all_names[0] = user_name
other_name = input('Напиши сюда имена каждого из игроков по одному. Когда закончишь, напиши "конец".\n').lower()
if other_name in all_names:
    print('Такое имя уже существует')
else:
    all_names.append(other_name)

while other_name != 'конец':
    other_name = input().lower()
    if other_name in all_names:
        print('Такое имя уже существует')
        continue
    if other_name != 'конец':
        all_names.append(other_name)
for name in all_names:
    print(f'Игрок №{all_names.index(name)}: ', end='')
    print(name)
