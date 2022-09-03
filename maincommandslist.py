import sqlite3


def input_command():
    print('Введите команду\n')

    command = input().split(maxsplit=1)
    name = command[0]
    function = commands_function.get(name)

    try:
        body = command[1]
    except IndexError:
        body = None

    if function is None:
        print(f'Команда {name} не найдена\n')
        return

    function(body)


def help_c(command: str):
    print('Это небольшая программа для регистрации и идентификации пользователей посредством ID ключей by Axime')
    print("Список команд:")
    for keys in commands_function.keys():
        print(keys)


def list_users(command: str):
    con = sqlite3.connect('users.db')
    c = con.cursor()

    if command is None:
        c.execute("SELECT rowid, * FROM users")
    else:
        try:
            op, value = command.split()
            c.execute(f"SELECT rowid, * from users WHERE rowid {op} {value}")
        except Exception as e:
            print(e)

    items = c.fetchall()
    for item in items:
        id, name, work = item
        print(f'{id} {name} {work}')

    con.close()


def add_user(command: str):
    user, inf = command.split(' ')
    con = sqlite3.connect('users.db')

    c = con.cursor()

    c.execute("INSERT INTO users VALUES (?, ?)", (user, inf))

    print(f'Запись {user} {inf} добавлена')
    # После названия таблицы идут условия выборки
    # where
    c.execute("SELECT rowid, * FROM users WHERE rowid >= 1")
    print(c.fetchall())

    con.commit()

    con.close()


def create_table(command: str):
    pass


commands_function = {
    'help': help_c,
    'list': list_users,
    'add': add_user,
    'create_table': create_table
}
