import time
from time import sleep
import serial
import datetime
import os
#ser = serial.Serial("/dev/ttyS0", baudrate = 119047, parity=serial.PARITY_NONE)
sleep(30)
time_start = datetime.datetime.utcnow()
#time_start = time_start.timestamp()
os.mkdir('/home/pi/Data/data_'+str(time_start))

ser = serial.Serial("/dev/ttyS0", baudrate = 115200)

count=0
while True:

    if count==0:
        time_now = datetime.datetime.utcnow()
        time_now = time_now.timestamp()
       
        f = open("/home/pi/Data/data_"+str(time_start)+"/data_"+str(int(time_now))+".log","wb")

    rx_data = ser.readline()
    sleep(0.2)
    data_left = ser.inWaiting()
    rx_data += ser.read(data_left)
    
    f.write(rx_data)

    count=count+1

    if count==180:
        f.close()
        count=0
