from flask import Flask
import sqlite3

db_path = "test.db"

def find_followee(id_json):
    cnxn = sqlite3.connect(db_path)

    cursor = cnxn.cursor()

    cursor.execute(
        "SELECT followee FROM user_followings WHERE user_followings.follower = '{}'".format(id_json["uid"]))

    jsonify = ({
        "uids": []
    })

    res = cursor.fetchone()

    while res:
        print(str(res[0]))

        send_data = {
            "uid": str(res[0])
        }

        res = cursor.fetchone()

        jsonify["uids"].append(send_data)

    cursor.close()
    cnxn.close()

    return jsonify

