from flask import Flask
import sqlite3

db_path = "cafe.db"

def create_user(json_data):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        if(len(json_data["name"]) >= 20):
            return "name is too long"
        if(len(json_data['uid']) >= 40):
            return "uid is too long"
        cur.execute(
            "INSERT into users (name,uid) VALUES ('{}','{}');".format(json_data["name"],json_data['uid'])
        )
        con.commit()

        # res = cur.fetchall()
        # print(res)
        cur.close()
        con.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"
