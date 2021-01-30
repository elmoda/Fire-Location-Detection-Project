import serial
import time
import string
import pynmea2
import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = '1234'
                       , db='raspi_db')
curs = conn.cursor()

sql ="""insert into location(longitude, latitude)  values(%s, %s)"""

 

def gps():
        try:
                while True:
                        port="/dev/ttyAMA0"
                        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
                        dataout = pynmea2.NMEAStreamReader()
                        newdata=ser.readline()

                        if newdata[0:6] == "$GPRMC":
                                newmsg=pynmea2.parse(newdata)
                                lat=newmsg.latitude
                                lng=newmsg.longitude
                                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                                print(gps)
                                str_lat = str(lat)
                                str_lng = str(lng)
                                curs.execute(sql,(str_lng, str_lat))
                                rs=curs.fetchall()
                                conn.commit()
                                time.sleep(15)
        finally:
                conn.close()


