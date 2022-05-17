from flask import Flask
import sqlite3

db_path = "cafe.db"


def photorefe_to_cafeid(photorefe):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        cur.execute(
            "select cafeid from photos where photoreference LIKE '{}';".format(str(photorefe))
        )
        data = cur.fetchall()
        print(data[0][0])
        con.commit()
        cur.close()
        con.close()
        jsonify = ({
            "cafeid":data[0][0]
        })
        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"
