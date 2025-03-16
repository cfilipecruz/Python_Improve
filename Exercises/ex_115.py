from modules.ex_115 import menu
from modules.ex_115 import colors
from modules.ex_115 import users

while True:
    menu.display()
    menu_choice = 4
    try:
        menu_choice = int(input(colors.colorfy('Escolha uma opção do menu: ','yellow')))
    except ValueError:
        print(f'The option "{menu_choice}" is not valid."')
    else:
        if menu_choice == 1:
            users.check_users()
        elif menu_choice == 2:
            try:
                name = str(input(colors.colorfy('Nome: ','green')))
            except KeyboardInterrupt:
                print(f'The user ended the program')
            try:
                age = int(input(colors.colorfy('Age: ','green')))
            except ValueError:
                print(f'The age must be an integer.')
            except KeyboardInterrupt:
                print(f'The user ended the program')
            else:
                users.get_new_user(name, age)

        elif menu_choice == 3:
            print(colors.colorfy('Program Finished', 'magenta'))
            break


