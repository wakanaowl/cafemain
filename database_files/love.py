from flask import Flask
import sqlite3

db_path = "test.db"

def love_cafes(jsondata):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        "PRAGMA foreign_keys = ON;"
    )
    con.commit()
    try:
        if(len(jsondata['uid']) >= 40):
            return "uid is too long"
        if(len(jsondata['cafeid']) >= 40):
            return "cafeid is too long"
        cur.execute(
            "INSERT love_cafes (cafeid,uid) VALUES ('{}','{}');".format(jsondata['cafeid'],jsondata['uid'])
        )
        con.commit()
        cur.close()
        con.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"