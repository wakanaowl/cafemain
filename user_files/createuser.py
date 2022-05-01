import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'

def create_user(json_data):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                         ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
    cur = conn.cursor()
    try:
        if(len(json_data["name"]) >= 20):
            return "name is too long"
        if(len(json_data['uid']) >= 40):
            return "uid is too long"
        cur.execute(
            "INSERT users (name,uid) VALUES ('{}','{}');".format(json_data["name"],json_data['uid'])
        )
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"
