import sqlite3

con = sqlite3.connect('cafe.db')
"create table users(uid varchar(40) PRIMARYKEY, name varchar(20), unique(uid))"
cur = con.cursor()
cur.execute(
    "SELECT name , Y.cafeid , photoreference, Y.uid  FROM users X   INNER JOIN visited_cafes Y ON Y.uid = X.uid INNER JOIN photos ON photos.cafeid = Y.cafeid ORDER BY name DESC;"
    )
con.commit()

res = cur.fetchall()
print(res)

con.commit()

con.close()

