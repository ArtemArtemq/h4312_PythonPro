import sqlite3

connection = sqlite3.connect("itstepDB.sl3, 5")
cur = connection.cursor()
# створення таблиці з ім'ям first_table одним полем name
# cur.execute("CREATE TABLE first_table(name TEXT);")
# вставлення в тіблицю first_table значення ('Artem') в поле name
cur.execute("INSERT INTO first_table(name) VALUES ('Artem');")
connection.commit()
# отримуємо і друкуємо значення з таблиці
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
result = cur.fetchall()
print(result)
connection.commit()