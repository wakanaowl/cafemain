from flask import Flask
import sqlite3

db_path = "cafe.db"

def follow(followee,follower):
    con = sqlite3.connect(db_path)
    cur = con.cursor()


    cur.execute(
    "PRAGMA foreign_keys = ON;"
        )
    con.commit()
    try:
        if(len(followee) >= 40):
            return "followee is too long"
        if(len(follower) >= 40):
            return "follwer is too long"
        cur.execute(
            "INSERT into user_followings (followee,follower) VALUES ('{}','{}');".format(followee,follower)
        )
        con.commit()
        cur.close()
        con.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"
