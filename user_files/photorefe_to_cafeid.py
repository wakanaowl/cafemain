import json
from flask import jsonify
import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'


def photorefe_to_cafeid(photorefe):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                          ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
    cur = conn.cursor()
    try:
        cur.execute(
            "select cafeid from photos where photoreference LIKE '{}';".format(str(photorefe))
        )
        data = cur.fetchall()
        print(data[0][0])
        conn.commit()
        cur.close()
        conn.close()
        jsonify = ({
            "cafeid":data[0][0]
        })
        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"
