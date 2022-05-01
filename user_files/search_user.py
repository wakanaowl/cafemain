import json
import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'

def search_users(jsondata):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                         ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
    cur = conn.cursor()
    try:
        if(len(jsondata) >= 40):
            return "uid is too long"
        print(jsondata)
        cur.execute(
            "select * from users where uid = '{}'".format(str(jsondata))
        )
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        print(data)

        for i in data:
            print(i[1])

        jsonify = ({
            "name":str(i[1])
        })

        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"