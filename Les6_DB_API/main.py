import mysql.connector

db = mysql.connector.connect(user="root", password="Qawasadedrdf102030", host="127.0.0.1", database="my_users")
cursor = db.cursor()
phone = "+380977456929"
query = 'SELECT * FROM users WHERE phone = "%s"' % phone
cursor.execute(query)
for (fname, lname, year, mail, phone) in cursor:
    print(fname, lname, year, mail, phone)
db.close()
