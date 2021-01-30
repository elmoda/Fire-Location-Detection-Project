import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = '1234'
		       , db='raspi_db')
curs = conn.cursor()

sql = "select * from flame_sensor;"

curs.execute(sql) # querry start

rows = curs.fetchall() # patch for data

for i in rows :
	print(i)

conn.close()


