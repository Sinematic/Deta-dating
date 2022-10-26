import sqlite3


class Queries:

    def __init__(self):
        try:
            cnx = sqlite3.connect('users.db')
            cursor = cnx.cursor()

        except BaseException as e:
            print(f" Erreur ! {e}")
            