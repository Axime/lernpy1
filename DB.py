import sqlite3


class DBclass:
    def check(self, name = None, password=None):

        con = sqlite3.connect('users.db')
        c = con.cursor()
        print(f"{name}{password}")

        c.execute(f"SELECT Name, Password FROM test_for_DBEditor WHERE Name = '{name}' and Password = '{password}'")

        if c.fetchone() is None:
            print("Unknown login and password")
            return False
        else:
            print(f"User:{name} Password:{password}")
            return True