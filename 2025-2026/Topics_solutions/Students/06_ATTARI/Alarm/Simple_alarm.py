import time
from datetime import datetime
import sys

def play_sound():
    if sys.platform.startswith("win"):
        import winsound
        for _ in range(5):
            winsound.Beep(1000, 500)
    else:
        print("\a")

print("=== Alarm Clock ===")
alarm_time = input("Set alarm time (HH:MM:SS): ")

try:
    datetime.strptime(alarm_time, "%H:%M:%S")
except:
    print("Invalid format. Use HH:MM:SS")
    exit()

print("Alarm set for:", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time, end="\r")

    if current_time == alarm_time:
        print("\n⏰ Alarm! Time to wake up!")
        play_sound()
        break

    time.sleep(1)
