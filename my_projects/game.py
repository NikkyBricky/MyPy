# Бунин Николай, 21 группа
print('Привет! Я тут подготовил для тебя одну игру.')

choice = input('Не хочешь сыграть?\n'
               '1 - да\n'
               '2 - нет\n')
if choice == '1':
    alive = ''
    print('А? Что это? Где ты? Ты вдруг проснулся на корабле, судя по всему какого-то ювелира, потому что человек за штурвалом уж очень похож на него.\n'
          'Но отчего на его лице такой ужас?\n'
          'Вдруг справа от тебя происходит взрыв, и ты видишь, как корабль пиратов столкнулся с твоим, и пираты вот-вот нагрянут.')
    weapon = input('У тебя есть всего пара секунд, чтобы что-то предпринять, но с пустыми руками ты ничего не сделаешь.\n'
                   'Ты смотришь вокруг и видишь перед собой столик с тремя предметами.\n'
                   'О нет! Один из пиратов уже прямо у тебя за спиной! У тебя нет времени на размышления! Забрать все ты не успеешь..\n'
                   'Скорее возьми что-нибудь!\n'
                   'Схватить:\n'
                   '1 - пистолет\n'
                   '2 - карту сокровищ\n'
                   '3 - удостоверение генерала\n')
    if weapon != '1' and weapon != '2' and weapon != '3':
        print('Нет такого ответа. Попробуй снова.')
    else:
       print('Теперь нужно решить, что делать дальше.\n'
                       'Ты можешь:\n'
                       '1 - прыгнуть за борт\n'
                       '2 - побежать в трюм\n'
                       '3 - сдаться пиратам')
       if weapon == '1':
            print('4 - выстрелить в пирата')
       action = input()
       if action == '1' and weapon == '1':
           print('Ты плыл и потерял сознание от нехватки сил.\n'
                 'Через некоторое время тебя выбросило на остров. Ты бродил по острову и, вдруг из кустов на тебя выпрыгнуло непонятное животное.\n'
                 'Хорошо, что у тебя был с собой пистолет, и ты смог с ним справиться. Потом ты случайно наткнулся на рыбацкий домик.\n'
                 'Вдруг вышел мужчина с ружьем. Он увидел у тебя в руке пистолет и, подумав, что ты хочешь его ограбить, застрелил тебя.')
           alive = False
       elif action == '1' and weapon == '2':
           print('Ты плыл и потерял сознание от нехватки сил.\n'
                 'Через некоторое время тебя выбросило на остров. Вдруг ты понял, что карта, которую ты взял со стола, является картой этого острова.\n'
                 'На карте стоял крестик, и ты отправился на поиски.\n'
                 'Дойдя до места назначения, ты увидел не сундук с сокровищами, а рыбацкий домик.\n'
                 'Вдруг незнакомец выскочил из этого домика с ружьем. Он взглянул на тебя и, заметив карту, удивился.\n'
                 'Ты рассказал ему все, как есть, и он сначала не поверил тебе,а потом, удостоверившись,что ты не грабитель, помог добраться до дома.')
           alive = True
       elif action == '1' and weapon == '3':
          choice_island = input('Ты плыл и потерял сознание от нехватки сил.\n'
                 'Через некоторое время тебя выбросило на остров. Ты бродил, бродил и случайно наткнулся на рыбацкий домик.\n'
                 'Вдруг вышел мужчина с ружьем. Он с удивлением посмотрел на тебя и спросил, кто ты.\n'
                 '1 - представиться генералом, показав удостоверение, и потребовать помощи.\n'
                 '2 - спрятать удостоверение, рассказать, что случилось, и попросить помощи.\n')
          if choice_island == '1':
              print('Оказалось, что незнакомец знал этого генерала. Он решил, что ты мошенник, и застрелил тебя.')
              alive = False
          elif choice_island == '2':
              print('Ты рассказал ему все, как есть, и он сначала не поверил тебе, а потом, удостоверившись,что ты не мошенник, помог добраться до дома.')
              alive = True
          else:
              print('Нет такого ответа. Попробуй снова.')
       elif action == '2':
           place = input('Что-ж, в трюме оказалось не так много мест,где можно спрятаться, а именно:\n'
                             '1 - в темнице\n'
                             '2 - за лестницей в трюм\n'
                             '3 - в комнате с украшениями\n')
           if place == '1':
               print('О нет! После того, как ты зашел в темницу, корабль пошатнулся и дверь за тобой захлопнулась.\n'
                     'Пираты обшарили трюм, не обращая на тебя внимание, ведь считали, что ты простой заключенный.\n'
                     'Потом, забрав все богатства, они потопили корабль, а ты утонул.')
               alive = False
           elif place == '2':
               action_in_place = input('Спустившись в трюм, пираты не заметили тебя.\n'
                     'Это твой шанс сбежать!\n'
                     '1 - побежать наверх\n'
                     '2 - остаться и попытаться разобраться с пиратами\n')
               if action_in_place == '1':
                    print('Оказалось, что наверху караулил еще один пират.')
                    if weapon == '1':
                        print('Хорошо, что ты взял с собой пистолет. Одним метким выстрелом ты поразил своего оппонента и, наконец, выбрался наружу.')
                        action_outside = input('Что делать дальше?\n'
                                                   '1 - прыгнуть за борт\n'
                                                   '2 - попытаться перехватить управление пиратским кораблем и уплыть.\n'
                                                   '3 - запереть пиратов в трюме и ждать помощи\n')
                        if action_outside == '1':
                            print('Ты плыл и потерял сознание от нехватки сил.\n'
                                  'Через некоторое время тебя выбросило на остров. Ты бродил, бродил и случайно наткнулся на рыбацкий домик.\n'
                                  'Вдруг вышел мужчина с ружьем. Он увидел у тебя в руке пистолет и, подумав, что ты хочешь его ограбить, застрелил тебя.')
                            alive = False
                        elif action_outside == '2':
                            print('Но тут ты понял, что совсем не знаешь как управлять пиратским кораблем, и поэтому не смог сдвинуться с места.\n'
                             'А пираты, услышав выстрел, сразу ринулись наверх и, увидев, что ты делаешь, пристрелили тебя.')
                            alive = False
                        elif action_outside == '3':
                            print('Ты ждал в течение 3 часов, и вдруг недалеко от тебя показался маленький парусник. Ты закричал, чтобы тебя заметили.\n'
                                  'И тебя действительно заметили!\n'
                                  'Правда.. Увидев пиратский флаг, хотели было уплыть, но у тебя каким-то образом получилось вкратце, с криком рассказать им, что случилось.\n'
                                  'Ты быстро прыгнул за борт, приплыл к паруснику и был доставлен домой в тот же день.')
                            alive = True
                        else:
                            print('Нет такого ответа. Попробуй снова.')
                    elif weapon == '2':
                        print('А ты, представившись таким же пиратом как он, показал ему карту сокровищ и сказал, что скоро будете туда отправляться.')
                        action_outside = input('Это твой шанс! Скорее решай, что делать, пока он ничего не заподозрил:\n'
                                                   '1 - прыгнуть за борт\n'
                                                   '2 - попытаться перехватить управление пиратским кораблем и уплыть.\n')
                        if action_outside == '1':
                            print('Ты плыл и потерял сознание от нехватки сил.\n'
                                  'Через некоторое время тебя выбросило на остров. Вдруг ты понял, что карта, которую ты взял со стола, является картой этого острова.\n'
                                  'На карте стоял крестик, и ты отправился на поиски.\n'
                                  'Дойдя до места назначения, ты увидел не сундук с сокровищами, а рыбацкий домик.\n'
                                  'Вдруг незнакомец выскочил из этого домика с ружьем. Он взглянул на тебя и, заметив карту, удивился.\n'
                                  'Ты рассказал ему все, как есть, и он сначала не поверил тебе,а потом, удостоверившись,что ты не грабитель, помог добраться до дома.')
                            alive = True
                        elif action_outside == '2':
                            print('Но тут ты понял, что совсем не знаешь как управлять пиратским кораблем.\n'
                                  'О чудо! На другой стороне карты была инструкция по управлению кораблем!\n'
                                  'Ты быстро все прочитал и уплыл на пиратском корабле домой.')
                            alive = True
                        else:
                            print('Нет такого ответа. Попробуй снова.')

                    elif weapon == '3':
                        print('Ты показал ему удостоверение генерала и был взят в заложники.\n'
                              'Вернувшись в город, пираты потребовали за тебя выкуп.\n'
                              'Генерал, чье имя было указано в удостоверении был лучшим другом городничего, и он сразу дал за тебя выкуп.\n'
                              'Потом, узнав кого он спас и почему, возложил все свои силы на поимку тех пиратов.\n'
                              'По-тихоньку он излавливал их по одному в разных точках мира.\n'
                              'И, наконец, через 2 года поймал всех. А ты за это время смог вернуться к нормальной жизни.')
                        alive = True
                    else:
                        print('Нет такого ответа. Попробуй снова.')
               elif action_in_place == '2' and weapon == '1':
                   print('Подкараулив капитана пиратов, ты выстрелил в него и попал ему прямо в глаз!\n'
                         'Как метко! Но вот только ты забыл, что там было еще 10 пиратов..\n'
                         'После такой проделки на тебе не осталось живого места.')
                   alive = False
               elif action_in_place == '2':
                   print('К сожалению, твоих собственных сил хватило лишь, чтобы толкнуть капитана пиратов.\n'
                         'Но после такой выходки на тебе не осталось живого места..')
                   alive = False
               else:
                   print('Нет такого ответа. Попробуй снова.')
           elif place == '3':
               print('Наверное, ты забыл, за чем обычно охотятся пираты..\n'
                     'Конечно же, они сразу пошли в эту комнату и не оставили тебе ни шанса на спасение..')
               alive = False
           else:
               print('Нет такого ответа. Попробуй снова.')
       elif action == '3':
           if weapon == '1':
               print('К сожалению, при тебе не оказалось ничего такого, что могло бы заставить пиратов взять тебя в заложники, а не убить..')
               alive = False
           elif weapon == '2':
               choice_map = input('Обыскивая тебя, пираты нашли карту и спросили, на что она указывает.\n'
                                      '1 - сказать, что не знаешь\n'
                                      '2 - на сокровища\n')
               if choice_map == '1':
                   print('К сожалению, при тебе не оказалось ничего такого, что могло бы заставить пиратов взять тебя в заложники, а не убить..')
                   alive = False
               elif choice_map == '2':
                   print('Когда пираты приплыли с тобой на остров, который был нарисован на карте, то пошли на точку, указанную там.\n'
                         'Но вместо сокровищ они нашли там лишь рыбацкий домик.\n'
                         'Из него выбежал незнакомец и попытался разобраться с пиратами.\n'
                         'У него ничего не получилось, а ты был убит за то, что соврал пиратам, ведь там не было никаких сокровищ.')
                   alive = False
               else:
                   print('Нет такого ответа. Попробуй снова.')
           elif weapon == '3':
               print('Пираты проверили каждого из тех, кто был на корабле.\n'
                     'Ты показал им удостоверение генерала и был взят в заложники. Остальных ждала более жалкая участь..\n'
                     'Вернувшись в город, пираты потребовали за тебя выкуп.\n'
                     'Генерал, чье имя было указано в удостоверении был лучшим другом городничего, и он сразу дал за тебя выкуп.\n'
                     'Потом, узнав кого он спас и почему, возложил все свои силы на поимку тех пиратов.\n'
                     'По-тихоньку он излавливал их по одному в разных точках мира.\n'
                     'И, наконец, через 2 года поймал всех. А ты за это время смог вернуться к нормальной жизни.')
               alive = True
           else:
               print('Нет такого ответа. Попробуй снова.')
       elif action == '4' and weapon == '1':
           print('Ты резко обернулся лицом к пирату и выстрелил.\n'
                 'Но вот неудача! Промах!\n'
                 'Пират такой ошибки не простил и ответным ударом пристрелил тебя.')
           alive = False
       else:
           print('Нет такого ответа. Попробуй снова.')
    if alive:
        print('')
        print('Поздравляю! Ты прошел мой квест! Благодарю за участие.\n'
              'А сможешь найти остальные хорошие концовки?')
        good_endings = input('Как найдешь все, можешь вписать сюда их количество:\n')
        if good_endings == '7':
            print('Ура ура! Все хорошие концовки найдены! Ты молодец!')
        elif good_endings.isdigit():
            print('Неа! Попробуй снова.')
        else:
            print('Это ведь не число! Попробуй снова.')
    elif alive == False:
        print('')
        print('В этот раз ты проиграл. Поопробуй еще раз.')

elif choice == '2':
    print('Жаль! Если захочешь поиграть, я всегда здесь.')
else:
    print('Нет такого ответа. Попробуй снова.')



