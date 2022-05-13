from traceback import print_tb
import pyodbc
import json
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = 'aH9kRZur'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)

cursor = cnxn.cursor()

cursor.execute(
    "SELECT name , Y.cafeid , photoreference  FROM users X INNER JOIN user_followings ON X.uid = user_followings.followee AND user_followings.follower = 'USER' INNER JOIN visited_cafes Y ON Y.uid = X.uid INNER JOIN photos ON photos.cafeid = Y.cafeid ORDER BY name DESC")

res = cursor.fetchall()
json_ = ({
    "datas":[]
})



late = res[0][0]

photos = []
len = len(res)
loop=0
for i in res:
    loop+=1
    # print(i[0],i[1],i[2])
    if i[0] != late:
        jsonify = ({
            "name":late,
            "phtotos":photos
        })
        json_['datas'].append(jsonify)
        # print(i[2])
        photos = []
    elif loop == len:
        jsonify = ({
            "name":late,
            "phtotos":photos
        })
        json_['datas'].append(jsonify)
        # print(i[2])
        photos = []
    else:
        print(i[0])
        photos.append(i[2])
    late = i[0]    

print(json_)

cursor.close()
cnxn.close()
