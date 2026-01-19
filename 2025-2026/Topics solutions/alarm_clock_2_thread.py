# Build an alarm clock where users can set a specific time for the alarm to go off.
# The program will continuously check the current time and trigger the alarm when the set time is reached.
# The program should be able to handle different time formats and should be able to run indefinitely until the user manually stops it.
# The program should also be able to handle different time zones and should handle only sound alarms.

import time
from datetime import datetime
import winsound   # For sound alarm on Windows
import threading  # For running the alarm in a separate thread
def set_alarm(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            trigger_sound_alarm()
            break
        time.sleep(1)  # Check every 30 seconds

def trigger_sound_alarm():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 4000  # Set Duration To 4000 ms == 4 seconds
    winsound.Beep(frequency, duration)

alarm_time = input("Enter the alarm time (HH:MM in 24-hour format): ")
alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time,))
alarm_thread.start()
print("Alarm set for", alarm_time)
alarm_thread.join()



# Note: Make sure to run this code on a Windows machine as winsound is specific to
# Windows. Also, ensure your system volume is up to hear the alarm sound.

