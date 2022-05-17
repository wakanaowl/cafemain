from flask import Flask
import sqlite3

db_path = "cafe.db"

def useralldata(uid):
    con = sqlite3.connect(db_path)

    jsonify = ({
        "data":[],
        "userinfo":[],
        "followerusers":[],
        "followeeusers":[]

    })
    
    cur = con.cursor()
    try:
        if(len(uid) >= 40):
            return "follwer is too long"
        cur.execute(
            "select * from users AS T1 INNER JOIN visited_cafes AS T2 ON T1.uid = T2.uid INNER JOIN cafe_table AS T4 ON T2.cafeid = T4.cafeid where T1.uid = '{}';".format(
                uid
            )
        )
        
        # INNER JOIN photos AS T5 ON T2.cafeid = T5.cafeid
        data = cur.fetchall()
        con.commit()

        print(1)

        cur.execute(
            "select * from users AS T1 INNER JOIN user_followings AS T2 ON T1.uid = T2.followee where T1.uid = '{}';".format(
                uid
            )
        )
        followeeusers = cur.fetchall()
        con.commit()

        cur.execute(
            "select COUNT(*) from users AS T1 INNER JOIN visited_cafes AS T2 ON T1.uid = T2.uid where T1.uid = '{}';".format(
                uid
            )
        )
        visitcafes = cur.fetchall()
        con.commit()

        print(2)

        cur.execute(
            "select * from users AS T1 INNER JOIN user_followings AS T2 ON T1.uid = T2.follower where T1.uid = '{}';".format(
                uid
            )
        )
        followerusers = cur.fetchall()
        con.commit()

        print(3)

        cur.execute(
            "select name from users where uid = '{}';".format(
                uid
            )
        )
        name = cur.fetchall()
        con.commit()

        print(4)

        cur.execute(
            "select COUNT(*) from users AS T1 INNER JOIN user_followings AS T2 ON T1.uid = T2.followee where T1.uid = '{}';".format(
                uid
            )
        )
        follower = cur.fetchall()
        con.commit()

        print(5)

        cur.execute(
            "select COUNT(*) from users AS T1 INNER JOIN user_followings AS T2 ON T1.uid = T2.followee where T1.uid = '{}';".format(
                uid
            )
        )
        followee = cur.fetchall()
        con.commit()



        print(follower[0][0],followee[0][0],visitcafes[0][0])

        userinfo = ({
            "userinfo":{
                "followeenum":follower[0][0],
                "followernum":followee[0][0],
                "username":name[0][0],
                "visitedcafes": visitcafes[0][0]
            }
        })
        jsonify["userinfo"].append(userinfo)

 
        for i in followerusers:
            print(i)
        for i in followeeusers:
            print(i)

        # print(data)

        # ('AAA-BBB-CCC', '実験君', 'd45d5df3-020d-40d0-b1b1-b7a7f56b4604', 'AAA-BBB-CCC', 'd45d5df3-020d-40d0-b1b1-b7a7f56b4604', 'https://www.dotcomspacetokyo.com/', '6渋谷区神宮前１丁目１９?１９ エリンデール神宮前 B1F', 'dotcom space Tokyo', 139.7036697, 35.6718711, 'https://maps.google.com/?cid=2553509413390461235')
        for i in data:
            cur.execute("select * from photos where cafeid = '{}';".format(i[2]))
            photo = cur.fetchall()
            con.commit()
            photos = []
            for l in photo:
                photos.append(str(l[1]))

            # print(photos)
                
            adddata = ({
                "cafename":i[7],
                "website":i[5] ,
                "address": i[6],
                "googlelink": i[10],
                "cafeid": i[4],
                "photos": photos
                })
            jsonify["data"].append(adddata)
        
        

            
        cur.close()
        con.close()
        return jsonify
    except Exception as e:
        print("err:" + str(e))
        return "err"
