from flask import Flask
import sqlite3

db_path = "test.db"

def follow_infomation(id_json):

    cnxn = sqlite3.connect(db_path)
    
    cursor = cnxn.cursor()

    cursor.execute(
        "SELECT name FROM users INNER JOIN user_followings ON users.uid = user_followings.followee AND user_followings.follower = '{}'".format(id_json["uid"]))

    jsonify = ({
        "names": []
    })

    res = cursor.fetchone()

    while res:
        print(str(res[0]))

        send_data = {
            "name": str(res[0])
        }

        res = cursor.fetchone()

        jsonify["names"].append(send_data)

    cursor.close()
    cnxn.close()

    return jsonify
