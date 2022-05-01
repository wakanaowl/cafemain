import pyodbc

server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'

def follow(followee,follower):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                         ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
    cur = conn.cursor()
    try:
        if(len(followee) >= 40):
            return "followee is too long"
        if(len(follower) >= 40):
            return "follwer is too long"
        cur.execute(
            "INSERT user_followings (followee,follower) VALUES ('{}','{}');".format(followee,follower)
        )
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except Exception as e:
        print("err:" + str(e))
        return "err"
