import sqlite3

con = sqlite3.connect('cafe.db')

con.execute("create table cafe_table(cafeid varchar(40) NOT NULL,website text NOT NULL,address text NOT NULL,cafename text NOT NULL,locationX float NOT NULL,locationY float NOT NULL,googlelink text NOT NULL, PRIMARY KEY (locationX,locationY))")

con.commit()

con.close()

