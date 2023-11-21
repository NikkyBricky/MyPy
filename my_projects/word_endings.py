new_users = [1]


def pluralize_users(num):
    num_ones = num % 10
    num_tens = ((num % 100) - (num % 10)) / 10
    adj_end = None
    noun_end = None
    if num_tens != 1:
        if num_ones == 1:
            adj_end = 'й'
            noun_end = 'ь'
        elif 2 <= num_ones <= 4:
            adj_end = 'х'
            noun_end = 'я'
        elif 0 <= num_ones <= 9:
            adj_end = 'х'
            noun_end = 'ей'
    else:
        adj_end = 'х'
        noun_end = 'ей'
    return [adj_end, noun_end]


if len(new_users) > 0:
    noun_ending = pluralize_users(len(new_users))
    adj_ending = pluralize_users(len(new_users))
    print(f"Сегодня подключилось {len(new_users)} новы{adj_ending[0]} пользовател{noun_ending[1]}")
else:
    print("Сегодня никто не подключился")
