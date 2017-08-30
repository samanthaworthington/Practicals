

def main():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")

    if username not in usernames:
        print("Access denied")
    else:
        print("Access Granted")

main()