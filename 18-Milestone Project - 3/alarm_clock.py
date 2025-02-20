
import datetime 
from datetime import time
import time
from playsound import playsound





def validate_time(want_alarm):
    if len(want_alarm) != 8:
        print("Wrong format, try again")

    else:
        if int(want_alarm[0:2]) > 23:
            print("Wrong HOUR format, try again")
        elif int(want_alarm[3:5]) > 59:
            print("Wrong MINUTES format, try again")
        elif int(want_alarm[6:8]) > 59:
            print("Wrong SECONDS format, try again")
        else:
            return 'OK'

while True:
    want_alarm = input("Set your alarm in standart form HH:MM:SS ")

    validate = validate_time(want_alarm.lower())
    if validate != 'OK':
        print(validate)
    else:
        print(f"Setting alarm for {want_alarm}")
        break

alarm_hour = want_alarm[0:2]
alarm_minute = want_alarm[3:5]
alarm_second = want_alarm[6:8]

while True:
    now = datetime.datetime.now()

    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")

    if current_hour == alarm_hour:
        if current_minute == alarm_minute:
            if current_second == alarm_second:
                print("Wake Up")
                playsound("/Users/vrubtsov/Downloads/open_source_projects/Complete-Python-3-Bootcamp/alarm-clock-beep-105903.mp3")
                break