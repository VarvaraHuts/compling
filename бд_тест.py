import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, firstName VARCHAR(100), secondName VARCHAR(30))')
con.commit()
cur.execute('INSERT INTO users (id, firstName, secondName) VALUES(NULL, "Guido", "van Rossum")')
con.commit()
print (cur.lastrowid)

cur.execute('SELECT * FROM users')
print (cur.fetchall())
con.close()
