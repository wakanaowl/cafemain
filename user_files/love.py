import json
import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'

def love_cafes(jsondata):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                         ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
    cur = conn.cursor()
    try:
        if(len(jsondata['uid']) >= 40):
            return "uid is too long"
        if(len(jsondata['cafeid']) >= 40):
            return "cafeid is too long"
        cur.execute(
            "INSERT love_cafes (cafeid,uid) VALUES ('{}','{}');".format(jsondata['cafeid'],jsondata['uid'])
        )
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"