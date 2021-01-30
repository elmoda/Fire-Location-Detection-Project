import time
import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = '1234'
                       , db='raspi_db')
curs = conn.cursor()


	#select value, longitude, latitude, date from gasvalue, location
	#group by value, longitude, latitude, date

sql ="""insert into grouping(value, longitude, latitude, date, ordernum)
	select g.value, l.longitude, l.latitude, l.date, l.ordernum
	from gasvalue AS g JOIN location AS l
	where g.ordernum = l.ordernum
	"""
a = 1

def f_group():
	global a
	try:
		while True:
			if a == 1 :
				curs.execute(sql)

				rs=curs.fetchall()

				conn.commit()

				time.sleep(1)

				a = 0
			else:

				sql2 = """truncate table grouping"""

				curs.execute(sql2)

		                rs=curs.fetchall()

		                conn.commit()

        		        time.sleep(1)

				a =1

	finally:
       	        conn.close()
