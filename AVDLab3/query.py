import mysql.connector
from Item import Item


class Query:
    def __init__(self, phone_list=[]):
        self.phone_list = phone_list
        self.db = mysql.connector.connect(user="root", password="Qawasadedrdf102030", host="127.0.0.1", database="my_users")
        self.cursor = self.db.cursor()
        self.ask_result = []

    def search(self, phones):
        self.phone_list = phones
        self.ask_result.clear()
        if len(self.phone_list) == 0:
            return False
        for phone in self.phone_list:
            query = 'SELECT * FROM users WHERE phone = "%s"' % phone
            self.cursor.execute(query)
            for (fname, lname, year, mail, phone) in self.cursor:
                item = Item(fname, lname, str(year), mail, phone)
                self.ask_result.append(item)
        return self.ask_result

    def __del__(self):
        self.db.close()
