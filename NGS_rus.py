from subprocess import call
from os import system, mkdir, path
from shutil import rmtree, copytree, copy
from time import sleep
from getpass import getuser
from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
system('color 6')


def process_running(processName):  # Проверка, запущена ли нойта
    for proc in process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return False

# Я хз почему, но класс с одной переменной, да, я ультратупой
class var:
    save_folder = 'C:\\Users\\' + getuser() + '\\AppData\\LocalLow\\Nolla_Games_Noita\\'


save_folders_amount = 5
if path.exists(var.save_folder + 'NGSload\\load02'):
    pass
else:
    mkdir(var.save_folder + 'NGSload')
    for i in range(save_folders_amount):
        save_folder = 'NGSload\\' + 'load0' + str(i + 1)
        mkdir(var.save_folder + save_folder)


def save(action='s', notch='0'):  # функция чтоб сохранить и загрузить файлы
    if action == 's': # s = save, else = load
        first_folder = var.save_folder + 'NGSload\\load0' + notch + '\\'
        second_folder = var.save_folder + 'save00\\'
    else:
        first_folder = var.save_folder + 'save00\\'
        second_folder = var.save_folder + 'NGSload\\load0' + notch + '\\'
    print('Закройте noita.exe для продолжения.') # или файлы могут повредиться
    while process_running('noita.exe'):
        sleep(0.1)
    if path.exists(first_folder + 'world\\'):  # удалить папку, если она пуста
        rmtree(first_folder)
        sleep(0.1)
        mkdir(first_folder)
    sleep(0.1)
    try:
        print('Копируем persistent') # копирование файлов в другую папку
        copytree(second_folder + 'persistent\\', first_folder + 'persistent\\')
        print('Копируем stats')
        copytree(second_folder + 'stats\\', first_folder + 'stats\\')
        print('Копируем world (может занять много времени)')
        copytree(second_folder + 'world\\', first_folder + 'world\\')
        print('Копируем player.xml')
        copy(second_folder + 'player.xml', first_folder + 'player.xml')
        print('Копируем world_state.xml')
        copy(second_folder + 'world_state.xml', first_folder + 'world_state.xml')
        print('Копируем session_numbers.salakieli')
        copy(second_folder + 'session_numbers.salakieli', first_folder + 'session_numbers.salakieli')
        print('Копируем mod_config.xml')
        copy(second_folder + 'mod_config.xml', first_folder + 'mod_config.xml')
        print('Операция завершена успешно!\n')
    except FileExistsError:  # Тупой ли я? Конечно же да! Я хз почему но без этой херни выдает ошибку
        rmtree(first_folder)
        sleep(0.1)
        mkdir(first_folder)
        save(action, notch)


while True:
    co = input('   Меню:\n'
               '     [1]  Сохранить\n'
               '     [2]  Загрузить\n'
               '     [3]  Удалить папку сохранения\n'
               '     [4]  Открыть noita.exe\n'
               '   Напишите цифру из [] чтобы продолжить\n>> ')
    if co == '1' or co == '2':  # Я такую хрень написал в Ноябре, но оставлю это не тронутым
        if co == '1':           # тк это бл работает
            co = 's'  # сохранить
        elif co == '2':
            co = 'l'  # загрузить
        print(f'   Выберите папку сохранения:')
        for i in range(save_folders_amount):
            save_folder = 'NGSload\\load0' + str(i + 1)
            if path.exists(var.save_folder + f'{save_folder}\\world\\'):
                if co == 'l':
                    print(f'  #{i + 1}')
                elif co == 's':
                    print(f'  #{i + 1} - FULL')
            else:
                if co == 's':
                    print(f'  #{i + 1}')
        co1 = input(f'[1-{save_folders_amount}] > ')
        save(co, co1)
    elif co == '3':  # Удалить файл сохранения
        print('   Выберите папку сохранения:')
        for i in range(save_folders_amount):
            if path.exists(var.save_folder + 'load0' + str(i + 1) + '\\world\\'):
                print(f'#{i + 1}')
        co1 = input(f'[1-{save_folders_amount}] > ')
        ch = input('  Вы уверены? Напишите что-то чтобы продолжить >')
        if ch != '':
            save_folder = 'NGSload\\load0' + co1
            print(save_folder)
            rmtree(var.save_folder + save_folder)
            sleep(0.1)
            mkdir(var.save_folder + save_folder)
            print('   Сохранение удалено навсегда...')
    elif co == '4':
        call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 881100")  # Ничего подозрительного

    else:
        print('   Вы мисскликнули?\n'
              '   Напишите число в [].')  # если ты напишешь 'dfgsdfhsadtjsdfgj'
    sleep(3)
    system('cls')
