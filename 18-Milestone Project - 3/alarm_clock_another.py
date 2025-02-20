import datetime
from datetime import time
from playsound import playsound

def validate_time(wanted_time):
    if len(wanted_time) != 8:
        print("ABORT, wrong format, try again")
    
    else:
        if int(wanted_time[0:2]) > 23:
            print("ABORT, wrong HOURS format,try again")
        elif int(wanted_time[3:5]) > 59:
            print("ABORT, wrong MINUTES format, try again")
        elif int(wanted_time[6:8]) > 59 :
            print("ABORT, wrong SECONDS format, try again")
        else:
            return"OK"

while True:
    wanted_time = input("Pick a time in standart format HH:MM:SS ")

    validate = validate_time(wanted_time.lower())
    if validate != 'OK':
        print(validate)
    else:
        print(f"Setting alarm for {wanted_time}")
        break

alarm_hour = wanted_time[0:2]
alarm_minute = wanted_time[3:5]
alarm_second = wanted_time[6:8]

while True:
    now = datetime.datetime.now()
     
    current_hour = now.strftime('%H')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')

    if current_hour == alarm_hour:
        if current_minute == alarm_minute:
            if current_second == alarm_second:
                print("Wake Up, sissy it's time to be a flashlight for your alpha cock")
                playsound("/Users/vrubtsov/Downloads/open_source_projects/Complete-Python-3-Bootcamp/alarm-clock-beep-105903.mp3")
                break