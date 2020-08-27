from gpiozero import LED
from gpiozero import MotionSensor
import sys
import time
import datetime
from datetime import date 
import os


def register():
    now = datetime.datetime.now()
    current_year = now.strftime('%Y')
    current_month = now.strftime('%m')
    current_date = now.strftime('%d')

    base_path = '/usr/src/app/record'
    data_path = os.path.join(base_path, current_year, current_month)

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    txts = open(data_path+'/'+current_date+'.txt', 'a')
    txts.write(now.strftime("%d/%m/%Y %H:%M:%S\n"))
    txts.close()

MS = MotionSensor(17)
while True:
    MS.wait_for_motion()
    print("Motion trigger")
    register()

    MS.wait_for_no_motion()
    print("Timeout is reached")