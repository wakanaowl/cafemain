from flask import Flask
import sqlite3

db_path = "cafe.db"

def search_users(jsondata):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        if(len(jsondata) >= 40):
            return "uid is too long"
        print(jsondata)
        cur.execute(
            "select * from users where uid = '{}'".format(str(jsondata))
        )
        data = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
        print(data)

        for i in data:
            print(i[1])

        jsonify = ({
            "name":str(i[1])
        })

        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"