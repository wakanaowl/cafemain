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

def fllowee_visited_cafes(flloweeids):

    cnxn = sqlite3.connect(db_path)
    cursor = cnxn.cursor()

    cafeids = []
    fllowee_cafes = [cafeids]

    for flloweeid in flloweeids:

        cursor.execute(
            'SELECT cafeid FROM visited_cafes JOIN users ON users.uid = visited_cafes.uid AND visited_cafes.uid = ?', flloweeid)

        # res = cursor.fetchall()

        res = cursor.fetchone()

        # for cafe_id in res :
        #     print(cafe_id)
        #     cafeids.append(str(cafe_id))

        while res:
            print(res[0])
            cafeids.append(str(res[0]))
            res = cursor.fetchone()

        fllowee_cafes.append(cafeids)

    cursor.close()
    cnxn.close()

    print('二つ目')

    print(fllowee_cafes)

    return fllowee_cafes


def fllowee_cafe_photos(followees_name,fllowees_cafes):

    cnxn = sqlite3.connect(db_path)
    
    cursor = cnxn.cursor()

    photos = []

    json_ = ({
        "datas": []
    })

    for row in range(len(fllowees_cafes)):

        name = followees_name[row]

        for col in range(len(fllowees_cafes[row])):

            cursor.execute(
                "SELECT TOP 1 photoreference FROM photos WHERE photos.cafeid = '{}'".format(fllowees_cafes[row][col]))
            res = cursor.fetchone()

            photos.append(res[0])

            # jsonify1["fllowee_cafe_photos"].append(send_data)

            jsonify = ({
                "name": name,
                "phtotos": photos
            })

        json_['datas'].append(jsonify)

        photos = []

    cursor.close()
    cnxn.close()

    print('三つ目')

    print(json_)

    return json_
