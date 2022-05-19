from traceback import print_tb
from flask import Flask
import sqlite3
import random

db_path = "cafe.db"

def timeline_info():

    cnxn = sqlite3.connect(db_path)
    cursor = cnxn.cursor()
    # "SELECT name , Y.cafeid , photoreference, Y.uid  FROM users X INNER JOIN user_followings ON X.uid = user_followings.followee AND user_followings.follower = '{}' INNER JOIN visited_cafes Y ON Y.uid = X.uid INNER JOIN photos ON photos.cafeid = Y.cafeid ORDER BY name DESC".format(json_data["uid"]))

    cursor.execute(
        "SELECT name , Y.cafeid , photoreference, Y.uid  FROM users X   INNER JOIN visited_cafes Y ON Y.uid = X.uid INNER JOIN photos ON photos.cafeid = Y.cafeid ORDER BY name DESC;")
    res = cursor.fetchall()
    json_ = ({
    "datas": []
    })

    # print(res)

    late = res[0][0]


    photos = []
    nagasa = len(res)
    loop = 0
    for i in res:
        loop += 1
        # print(i[0],i[1],i[2])
        if i[1] != late:
            jsonify = ({
                "name": i[0],
                "uid":i[3],
                "phtotos": photos
            })
            json_['datas'].append(jsonify)
            # print(i[2])
            photos = []
        elif loop == nagasa:
            jsonify = ({
                "name": i[0],
                "uid": i[3],
                "phtotos": photos
            })
            json_['datas'].append(jsonify)
            # print(i[2])
            photos = []
        else:
            # print(i[0])
            photos.append(i[2])
        late = i[1]

    cursor.close()
    cnxn.close()

    # print("jsondata",json_)

    return json_

timeline_info()
