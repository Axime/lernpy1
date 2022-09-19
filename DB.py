import sqlite3


class DBclass:
    def check(self, name = None, password=None):
        try:
            con = sqlite3.connect('users.db')
            c = con.cursor()
            print(f"{name} {password}")
            c.execute(f"SELECT Name, Password FROM test_for_DBEditor WHERE Name = '{name}' and Password = '{password}'")

            if c.fetchone() is None:
                print("Unknown login or password")
                con.close()
                return False

            else:
                print(f"User: {name}    Password: {password}")
                con.close()
                return True
        except Exception as e:
            print(e)


    def open_database_file(self, sourse=None):
        if sourse == None:
            print(f"File {sourse} not found")
        else:
            print(f"Open file {sourse}")