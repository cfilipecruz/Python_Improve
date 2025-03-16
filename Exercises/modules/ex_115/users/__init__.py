import json
import os
from ..colors import colorfy

file_path = 'modules/ex_115/users/users.txt'


def check_users():
    try:
        file = open(file_path, "r")
    except Exception as error:
        print('The file has an error or does not exists')
    else:
        users_dict_list = []
        for line in file:
            line = line.strip()
            name, age = line.split('.')
            users_dict_list.append({'Name': name, 'Age': age})

        for user in users_dict_list:
            print(f'{colorfy(user['Name'], 'cyan'):<20}', end='')
            print(f'{colorfy(user['Age'], 'green'):>20}')


def get_new_user(name, age):
    name = name.strip()
    create_new_user(name, age)


def create_new_user(name='unknwon', age=0):

    if os.path.exists(file_path):
        print("Reading file...")
    else:
        print('Creating file...')
        try:
            file = open(file_path, 'w')
        except Exception as error:
            print('The file path has an error or does not exists')

    try:
        print("Writing in file...")
        file = open(file_path, "a")
        file.write(f"{name}.{age}\n")
        file.close()
    except Exception as error:
        print(f'Not possible to create new user: {error}')
    else:
        print("User created successfully")

