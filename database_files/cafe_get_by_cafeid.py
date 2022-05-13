from flask import Flask
import sqlite3

db_path = "test.db"


def cafe_get_by_cafeid(cafeid):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        if(len(cafeid) >= 40):
            return "cafeid is too long"

        print(str(cafeid))
        cur.execute(
            "select * from cafe_table AS T1 INNER JOIN photos AS T2 ON T1.cafeid = T2.cafeid where T1.cafeid = '{}';".format(
                str(cafeid))
        )
        data = cur.fetchall()
        print(data)

        photos = []
        for i in data:
            print(i[8])
            photos.append(i[8])
        jsonify = ({
                "data": {
                    "cafeid":data[0][0],
                    "address": data[0][2],
                    "locationX": data[0][4],
                    "locationY": data[0][5],
                    "name": data[0][3],
                    "googlename": data[0][6],
                    "website": data[0][1],
                    "photos":photos
                }
            }
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"
