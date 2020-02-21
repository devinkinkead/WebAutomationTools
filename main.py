import EmailDeleter
import os
import getpass


def menu():
    print(f'{"Web Automator":*^30}')
    print('1. Yahoo Email Deleter')
    selection = input('Please select option (1): ')

    if selection == '1':
        os.system('clear')
        print(f'{"Yahoo Email Credentials":*^30}')
        print('')
        user = input('What is your username?: ')
        password = getpass.getpass('What is your password?: ')
        minutes = input('How many minutes to run program?: ')
        os.system('clear')
        try:
            minutes = float(minutes)
        except (TypeError, ValueError):
            print(f'{minutes} is not a valid number. Setting to default...')
            EmailDeleter.yahoo(user, password)
        else:
            EmailDeleter.yahoo(user, password, minutes)
    else:
        print(f'{selection} is invalid. Closing Program...')

# run menu


menu()
