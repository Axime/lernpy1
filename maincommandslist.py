import sqlite3

def input_command ():
    print('Введите команду\n')
    command = input()
    if command in fun:
        fun[command]()
    else:
        print(f'Команда {command} не найдена\n')

def help_c():
    print('Это небольшая программа для регистрации и идентификации пользователей посредством ID ключей by Axime')
    print("Список команд:")
    for keys in fun.keys():
        print(keys)
    print ('\n')

def list_users():
    pass
    '''
    with open('users.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)'''

def add_user():
    con = sqlite3.connect('users.db')

    c = con.cursor()

#    c.execute("""CREATE TABLE users (
#        id integer,
#        name text,
#        inf text
#    )""")

#    c.execute("INSERT INTO users VALUES (3, 'Махест', 'Самый лучший')")

    c.execute("SELECT * FROM users ")
    print(c.fetchone()[1])


    con.commit()

    con.close()



fun = {
    'help': help_c,
    'list': list_users,
    'add': add_user
}


