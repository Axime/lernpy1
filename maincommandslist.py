import sqlite3
import random


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
            op, value, table = command.split()
            c.execute(f"SELECT rowid, * from {table} WHERE rowid {op} {value}")
        except Exception as e:
            print(e)

    items = c.fetchall()

    for item in items:
        id, name, work = item
        print(f'{id} {name} {work}')

    con.close()


def add_user(command: str):
    if command is None:
        print('Введите имя и информацию пользователя')
    else:
        try:
            user, inf = command.split(' ')
        except Exception as e:
            print(e)

        con = sqlite3.connect('users.db')

        c = con.cursor()
        if command is None:
            print(f"Введите данные пользователя (add имя информация)\n")
        else:
            c.execute("INSERT INTO users VALUES (?, ?)", (user, inf))
            print(f'Запись {user} {inf} добавлена')

        # После названия таблицы идут условия выборки
        # where
        c.execute("SELECT rowid, * FROM users")
        print(c.fetchall())

        con.commit()

        con.close()


def create_table(command: str):
    table_name = command
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}' ''')

    if c.fetchone()[0] == 1:
        print(f'Таблица {table_name} уже существует.')
    else:
        c.execute(f"""
            CREATE TABLE {table_name} (
                name text,
                inf text            
            )
        """)

        print(f'Таблица {table_name} создана')

    print('Список таблиц\n')
    c.execute("SELECT name from sqlite_master where type= 'table' \n")
    print(c.fetchall())


def clear_table(command: str):
    if command is None:
        print('Введите название таблицы')
    else:
        try:
            table_name = command
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute(f'DROP TABLE IF EXISTS {table_name}')
            print(f'Таблица {table_name} удалена')
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


def table_list(command: str):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    print('Список таблиц')
    c.execute("SELECT name from sqlite_master where type= 'table' ")
    print(c.fetchall())
    conn.close()


def rand_int(command: str):
    if command is None:
        cod = random.randint(1, 500000)
    else:
        cod = random.randint(1, int(command))
    print(cod)
    return cod


def clear_lines_table(command: str):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    table_name = command
    if command is None:
        print("Введите название таблицы (ПРИМЕР: clear_table название_таблицы)")
    else:
        c.execute(f"DELETE FROM {table_name}")
        print(f"Из таблицы {table_name} удалено {c.rowcount} строк")
        conn.commit()


# command list
commands_function = {
    'help': help_c,
    'list': list_users,
    'add': add_user,
    'create_table': create_table,
    'rand': rand_int,
    'clear_lines_table': clear_lines_table,
    'table_list': table_list,
    'del_table': clear_table
}
