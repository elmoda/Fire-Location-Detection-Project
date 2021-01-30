import time
import os
import pymysql
from threading import Thread
from gpssensor import gps
from mq2 import gas
from groupby import f_group

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = '1234'
                       , db='raspi_db')
curs = conn.cursor()



def flame():
	f = open('flamesensor.py','rt')

def mq2():
	gas()

def gpssensor():
	gps()

def d_group():
	f_group()



if __name__ == '__main__':
	proc = Thread(target=mq2, args=())
        proc2 = Thread(target=gpssensor, args=())
	proc3 = Thread(target=d_group, args=())

        proc.start()
        proc2.start()
	proc3.start()

        #f.close()
        #g.close()

