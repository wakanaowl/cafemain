import sqlite3

con = sqlite3.connect('cafe.db')
"create table users(uid varchar(40) PRIMARYKEY, name varchar(20), unique(uid))"
cur = con.cursor()
cur.execute(
    "PRAGMA foreign_keys = ON;"
    )
con.commit()

res = cur.fetchall()
print(res)

con.commit()
cur = con.cursor()
cur.execute(
    "PRAGMA foreign_keys;"
    )

res = cur.fetchall()
print(res)

con.commit()

con.close()

