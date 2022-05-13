from flask import Flask
import sqlite3

db_path = "test.db"

def insert_users(jsondata):

    con = sqlite3.connect(db_path)
    con.execute("insert into users values('{}','{}')".format(jsondata['users']['name'],jsondata['users']['uid']))

    data = con.execute ("select * from users")

    for row in data:
        print(row)

    data.close()

    con.close()
