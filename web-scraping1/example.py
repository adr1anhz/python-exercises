import sqlite3


connection = sqlite3.connect("data")
cursor = connection.cursor()

#cursor.execute("SELECT * FROM events WHERE band='Lions'")
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(type(rows))
print(rows)
