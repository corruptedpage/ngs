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
    print('Copying persistent')
    shutil.copytree(die + 'persistent\\', die1 + 'persistent\\')

    print('Copying stats')
    shutil.copytree(die + 'stats\\', die1 + 'stats\\')

    print('Copying world (might take a while)')
    shutil.copytree(die + 'world\\', die1 + 'world\\')

    print('Copying player.xml')
    shutil.copy(die + 'player.xml', die1 + 'player.xml')

    print('Copying world_state.xml')
    shutil.copy(die + 'world_state.xml', die1 + 'world_state.xml')

    print('Copying session_numbers.salakieli')
    shutil.copy(die + 'session_numbers.salakieli', die1 + 'session_numbers.salakieli')

    print('Copying mod_config.xml')
    shutil.copy(die + 'mod_config.xml', die1 + 'mod_config.xml')

    print('Operation completed successfully!')


while 1 == 1:
    co = int(input('   Menu:\n'
                   '   1. Save\n'
                   '   2. Load\n'
                   '   3. delete save\n'
                   '   4. instructions\n'
                   '   IMPORTANT: TYPE A NUMBER OF THE OPTION YOU CHOSSE (1 FOR SAVING, ETC)\n'))
    if co != 3:
        if co == 1:
            co = 's'
        else:
            co = 'l'
        print(f'   Choose save file:')
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
        ch = input("   Are you sure? Press Enter if yes, type anything if you've changed your mind ")
        if ch == '':
            savenload(co, co1)
    elif co == 3:
        print('Choose save file:')
        for i in range(b_amount):
            if os.path.exists(var.die + 'load0' + str(i+1) + '\\world\\'):
                print(f'#{i+1}')
            else:
                pass
        co1 = input(f'[1-{b_amount}] >')
        ch = input('  Are you REALLY sure? Type "yes" to confirm ')
        if ch == 'yes':
            sovr = 'load0' + co1
            print(sovr)
            shutil.rmtree(var.die + sovr)
            time.sleep(0.1)
            os.mkdir(var.die + sovr)
            print('   This save file is now gone forever...')

    else:
        print('   Everything is easy: first you need to choose whether youd like to save or load your save file\n'
              '   next choose what file # you want.')
    time.sleep(3)
    os.system('cls')
