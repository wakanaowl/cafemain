import psycopg2

conn = psycopg2.connect(dbname='d59c5hsafrhv6v', user='rtravcrmmghrca', host='ec2-107-22-238-112.compute-1.amazonaws.com', port=5432, password='d09b4f9c0664fc89cbd0015ad008a09f06e96611b63ce1ecc9595595c1d7dfad')

cur = conn.cursor()

id = '123450'
na = 'nyaaa'

cur.execute("INSERT INTO users(name,uid) VALUES (%s,%s);", (na, id))
    
conn.commit()

cur.close()
conn.close()
