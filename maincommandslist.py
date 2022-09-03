import sqlite3
command = ""
def input_command ():
    global command
    print('Введите команду\n')
    command = input().split()
    if str(command[0]) in fun:
        fun[command[0]]()
    else:
        print(f'Команда {command} не найдена\n')
    return command

def help_c():
    print('Это небольшая программа для регистрации и идентификации пользователей посредством ID ключей by Axime')
    print("Список команд:")
    for keys in fun.keys():
        print(keys)

def list_users():
    con = sqlite3.connect('users.db')
    c = con.cursor()
    c.execute("SELECT rowid, * FROM users")

    items = c.fetchall()
    for item  in items:
        print(str(item[0]) + " " + item[1] + " " + item[2])
    con.commit()
    con.close()

def add_user():
    user = str(command[1])
    inf = str(command[2])
    con = sqlite3.connect('users.db')

    c = con.cursor()

#    c.execute("""CREATE TABLE users (
#        name text,
#        inf text
#    )""")

    c.execute("INSERT INTO users VALUES ('?', '?'), ("+(str(user)+","+str(inf)+")")) #<========== ТУТА


    print(f'Запись {user} {inf} добавлена')
#После названия таблицы идут условия выборки
#where
    c.execute("SELECT rowid, * FROM users WHERE rowid >= 1")
    print(c.fetchall())

    con.commit()

    con.close()
def create_table(name_table):
    pass

fun = {
    'help': help_c,
    'list': list_users,
    'add': add_user,
    'create table': create_table
}


