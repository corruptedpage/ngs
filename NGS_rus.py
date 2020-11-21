import shutil, os, time, getpass

os.system('color 6')
class var:
    die = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\LocalLow\\Nolla_Games_Noita\\'

b_amount = 5
if os.path.exists(var.die + 'load02'):
    pass
else:
    for i in range(b_amount):
        sovr = 'load0' + str(i+1)
        os.mkdir(var.die + sovr)


def savenload (sorv = 's', notch = '0'):
    if sorv == 's':
        die1 = var.die + 'load0' + notch + '\\'
        die = var.die + 'save00\\'
    else:
        die1 = var.die + 'save00\\'
        die = var.die + 'load0' + notch + '\\'
    if os.path.exists(die1 + 'world\\'):
        shutil.rmtree(die1)
        time.sleep(0.1)
        os.mkdir(die1)
    time.sleep(0.1)
    print('Копируем persistent')
    shutil.copytree(die + 'persistent\\', die1 + 'persistent\\')

    print('Копируем stats')
    shutil.copytree(die + 'stats\\', die1 + 'stats\\')

    print('Копируем world (Может занять много времени)')
    shutil.copytree(die + 'world\\', die1 + 'world\\')

    print('Копируем player.xml')
    shutil.copy(die + 'player.xml', die1 + 'player.xml')

    print('Копируем world_state.xml')
    shutil.copy(die + 'world_state.xml', die1 + 'world_state.xml')

    print('Копируем session_numbers.salakieli')
    shutil.copy(die + 'session_numbers.salakieli', die1 + 'session_numbers.salakieli')

    print('Копируем mod_config.xml')
    shutil.copy(die + 'mod_config.xml', die1 + 'mod_config.xml')

    print('Операция завершена успешно!')


while 1 == 1:
    co = int(input('   Меню:\n'
                   '   1. Сохранить\n'
                   '   2. Загрузить\n'
                   '   3. Удалить сохранение\n'
                   '   4. Инструкция\n'
                   ' ВАЖНО: ВЫБРАТЬ НОМЕР ОПЦИИ (1 ДЛЯ СОХРАНЕНИЯ, НАПРИМЕР)\n'))
    if co != 3:
        if co == 1:
            co = 's'
        else:
            co = 'l'
        print(f'   Выберите ячейку сохранения:')
        for i in range(b_amount):
            sovr = 'load0' + str(i+1)
            if os.path.exists(var.die + f'{sovr}\\world\\'):
                if co == 'l':
                    print(f'  #{i+1}')
                elif co == 's':
                    print(f'  #{i + 1} - FULL')
            else:
                if co == 's':
                    print(f'  #{i+1}')
        co1 = input(f'[1-{b_amount}] >')
        ch = input("   Вы уверены? Нажмите [Enter] ничего не вводя, если да. Введите что-то для отмены ")
        if ch == '':
            savenload(co, co1)
    elif co == 3:
        print('Выберите ячейку сохранения:')
        for i in range(b_amount):
            if os.path.exists(var.die + 'load0' + str(i+1) + '\\world\\'):
                print(f'#{i+1}')
            else:
                pass
        co1 = input(f'[1-{b_amount}] >')
        ch = input('  Вы ТОЧНО уверены? Напишите "да" чтобы продолжить ')
        if ch == 'да':
            sovr = 'load0' + co1
            print(sovr)
            shutil.rmtree(var.die + sovr)
            time.sleep(0.1)
            os.mkdir(var.die + sovr)
            print('   This save file is now gone forever...')

    else:
        print('   Все просто: необходимо выбрать сохранить или загрузить игру, потом выбрать ячейку для выгрузки файлов сохранения.'
              '   \n')
    time.sleep(3)
    os.system('cls')
