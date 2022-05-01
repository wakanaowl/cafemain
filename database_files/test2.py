import json
from flask import jsonify
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = 'aH9kRZur'


def my_visited_cafes(id_json):

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()

    print(format(id_json["uid"]))

    testtxt = format(id_json["uid"])

    cursor.execute(
        'SELECT cafeid FROM visited_cafes JOIN users ON users.uid = visited_cafes.uid AND visited_cafes.uid = ?', testtxt)

    # cursor.execute(
    #     "SELECT cafeid FROM visited_cafes JOIN users ON users.uid = visited_cafes.uid AND visited_cafes.uid = 'AAA-BBB-CCC'")
    cafeids = []

    res = cursor.fetchone()

    i = 0

    while res:
        cafeids.append(str(res[0]))
        res = cursor.fetchone()
        i += 1

    cursor.close()
    cnxn.close()

    return cafeids


def my_visited_photos(cafeids):

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()

    jsonify = ({
        "mycafe_photos": []
    })

    for cafeid in cafeids:
        print(cafeid)
        cursor.execute(
            'SELECT photoreference FROM photos WHERE photos.cafeid = ?', cafeid)
        res = cursor.fetchone()

        send_data = {
            "photo": str(res[0])
        }

        jsonify["mycafe_photos"].append(send_data)

    cursor.close()
    cnxn.close()

    # cursor.execute(

    return jsonify


def find_followeeee(id_json):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()

    testtxt = format(id_json["uid"])

    cursor.execute(
        'SELECT followee FROM user_followings WHERE user_followings.follower = ?', testtxt)
    # "SELECT followee FROM user_followings WHERE user_followings.follower = 'USER'")

    flloweeids = []

    res = cursor.fetchone()

    i = 0

    while res:
        flloweeids.append(str(res[0]))
        res = cursor.fetchone()
        i += 1

        res = cursor.fetchone()

    cursor.close()
    cnxn.close()

    print('一つ目')

    print(flloweeids)

    return flloweeids

def find_followee_name(id_json):

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()

    cursor.execute(
        "SELECT name FROM users INNER JOIN user_followings ON users.uid = user_followings.followee AND user_followings.follower = '{}'".format(id_json["uid"]))

    followee_names = []

    res = cursor.fetchone()

    while res:
        print(res)
        followee_names.append(str(res[0]))
        res = cursor.fetchone()

    cursor.close()
    cnxn.close()

    print('~~~~~~~~~~~~~~')

    print(followee_names)

    return followee_names

def fllowee_visited_cafes(flloweeids):

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
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

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
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
