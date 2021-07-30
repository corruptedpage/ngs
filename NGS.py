from subprocess import call
from os import system, mkdir, path
from shutil import rmtree, copytree, copy
from time import sleep
from getpass import getuser
from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
system('color 6')


def process_running(processName):  # check if noita is running
    for proc in process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return False

# idk why but yeah class for only one variable i am stupid as hell
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


def save(action='s', notch='0'):  # save and load func
    if action == 's': # s = save, else = load
        first_folder = var.save_folder + 'NGSload\\load0' + notch + '\\'
        second_folder = var.save_folder + 'save00\\'
    else:
        first_folder = var.save_folder + 'save00\\'
        second_folder = var.save_folder + 'NGSload\\load0' + notch + '\\'
    print('Close noita.exe to continue.') # or else files get corrupted
    while process_running('noita.exe'):
        sleep(0.1)
    if path.exists(first_folder + 'world\\'):  # delete the save folder if it is not empty
        rmtree(first_folder)
        sleep(0.1)
        mkdir(first_folder)
    sleep(0.1)
    try:
        print('Copying persistent') # copy the files to the second directory
        copytree(second_folder + 'persistent\\', first_folder + 'persistent\\')
        print('Copying stats')
        copytree(second_folder + 'stats\\', first_folder + 'stats\\')
        print('Copying world (might take a while)')
        copytree(second_folder + 'world\\', first_folder + 'world\\')
        print('Copying player.xml')
        copy(second_folder + 'player.xml', first_folder + 'player.xml')
        print('Copying world_state.xml')
        copy(second_folder + 'world_state.xml', first_folder + 'world_state.xml')
        print('Copying session_numbers.salakieli')
        copy(second_folder + 'session_numbers.salakieli', first_folder + 'session_numbers.salakieli')
        print('Copying mod_config.xml')
        copy(second_folder + 'mod_config.xml', first_folder + 'mod_config.xml')
        print('Operation completed successfully!\n')
    except FileExistsError:  # yeah am i stupid? Of course i am! Idk why but i got an error when i didn't have this shit
        rmtree(first_folder)
        sleep(0.1)
        mkdir(first_folder)
        save(action, notch)


while True:
    co = input('   Menu:\n'
               '     [1]  Save\n'
               '     [2]  Load\n'
               '     [3]  delete load folder\n'
               '     [4]  Open noita.exe\n'
               '   Type the number in [] to proceed\n>> ')
    if co == '1' or co == '2':  # i was too stupid when i coded it in November, but i decided to leave it like
        if co == '1':           # this cuz it fcking works lmao
            co = 's'  # save
        elif co == '2':
            co = 'l'  # load
        print(f'   Choose save file:')
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
    elif co == '3':  # delete save file
        print('Choose save file:')
        for i in range(save_folders_amount):
            if path.exists(var.save_folder + 'load0' + str(i + 1) + '\\world\\'):
                print(f'#{i + 1}')
        co1 = input(f'[1-{save_folders_amount}] > ')
        ch = input('  Are you sure? Type anything to confirm ')
        if ch != '':
            save_folder = 'NGSload\\load0' + co1
            print(save_folder)
            rmtree(var.save_folder + save_folder)
            sleep(0.1)
            mkdir(var.save_folder + save_folder)
            print('   This save file is now gone forever...')
    elif co == '4':
        call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 881100")  # nothing sus oficcer

    else:
        print('   Did you missclick?\n'
              '   Just choose what file # you want. type 1 and press enter')  # if you type 'dfgsdfhsadtjsdfgj'
    sleep(3)
    system('cls')
