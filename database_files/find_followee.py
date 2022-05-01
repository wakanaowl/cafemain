import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'


def find_followee(id_json):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
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


def follow_infomation(id_json):

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
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


def timeline_info(json_data):


    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)

    cursor = cnxn.cursor()

    cursor.execute(
    "SELECT name , Y.cafeid , photoreference  FROM users X INNER JOIN user_followings ON X.uid = user_followings.followee AND user_followings.follower = '{}' INNER JOIN visited_cafes Y ON Y.uid = X.uid INNER JOIN photos ON photos.cafeid = Y.cafeid ORDER BY name DESC".format(json_data["uid"]))

    res = cursor.fetchall()
    json_ = ({
    "datas": []
    })

    late = res[0][0]

    photos = []
    nagasa = len(res)
    loop = 0
    for i in res:
        loop += 1
        # print(i[0],i[1],i[2])
        if i[0] != late:
            jsonify = ({
                "name": late,
                "phtotos": photos
            })
            json_['datas'].append(jsonify)
            # print(i[2])
            photos = []
        elif loop == nagasa:
            jsonify = ({
                "name": late,
                "phtotos": photos
            })
            json_['datas'].append(jsonify)
            # print(i[2])
            photos = []
        else:
            # print(i[0])
            photos.append(i[2])
        late = i[0]

    cursor.close()
    cnxn.close()

    return json_
