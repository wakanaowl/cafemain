from flask import Flask
import sqlite3
import uuid

db_path = "cafe.db"

# def initialized():
#     conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
#                          ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             "create table cafe_table(cafeid char(40) NOT NULL,website text NOT NULL,address text NOT NULL,cafename text NOT NULL,locationX float NOT NULL,locationY float NOT NULL,googlelink text NOT NULL PRIMARY KEY (locationX,locationY));"
#         )
#     except Exception as e:
#         print("err:" + str(e))
#         return 1
#     return 0


def cafe_insert(json_data,userid):
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()
    uid = str(uuid.uuid4())
    try:
        # print(json_data['data'][0]['adress'], json_data['data'][0]['googlelink'], json_data['data'][0]['name'], json_data['data'][0]['website'], json_data['data'][0]['locationX'], json_data['data'][0]['locationY'])
        if(len(userid) >= 40):
            return "userid is too long"
        
        cur.execute(
            "INSERT INTO cafe_table (cafeid,address,googlelink,cafename,website,locationX,locationY) VALUES ('{}','{}','{}','{}','{}',{},{})".format(uid, json_data['data'][0]['adress'], json_data['data'][0]['googlelink'], json_data['data'][0]['name'], json_data['data'][0]['website'], json_data['data'][0]['locationX'], json_data['data'][0]['locationY']))
        conn.commit()
        print(json_data)
        for photo in json_data['photos']:
            print(photo)
            cur.execute(
                "INSERT INTO photos (cafeid,photoreference) VALUES ('{}','{}')".format(uid,photo)
            )

        cur.execute(
            "INSERT INTO visited_cafes (cafeid,uid) VALUES ('{}','{}')".format(uid,userid)
        )
        conn.commit()
        cur.close()
        conn.close()
        return "sucess"
    except Exception as e:
        print(str(e))
        try:
            cur.execute(
           "select cafeid from cafe_table where locationX = {} AND locationY = {}".format(
               json_data['data'][0]['locationX'], json_data['data'][0]['locationY'])
            )
            datas = cur.fetchall()
            conn.commit()
            cafeid = str(datas[0]).split("'")
            cur.execute(
                "INSERT INTO visited_cafes (cafeid,uid) VALUES ('{}','{}')".format(
                    cafeid[1], 2)
            )
            conn.commit()
            cur.close()
            conn.close()
            return "SUCCESS"
        except Exception as e:
            print(str(e))
            return "err"
