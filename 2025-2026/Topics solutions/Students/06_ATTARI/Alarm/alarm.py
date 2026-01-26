

import time
from datetime import datetime
import sys
import csv
import os

FILE_NAME = "alarms.csv"


# -------- SOUND --------
def play_sound():
    try:
        if sys.platform.startswith("win"):
            import winsound
            for _ in range(6):
                winsound.Beep(1200, 400)
        else:
            print("\a")
    except:
        print("Beep!")


# -------- CREATE CSV IF NOT EXISTS --------
def create_csv():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Alarm_Time"])
            writer.writerow(["00:5:00"])


# -------- READ ALARM FROM CSV --------
def read_alarm():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row["Alarm_Time"]


create_csv()
alarm_time = read_alarm()

print("=" * 45)
print("   ⏰ MODERN CLOCK & ALARM (READ FROM CSV) ⏰")
print("=" * 45)
print("Alarm loaded from CSV:", alarm_time)
print("You can edit alarms.csv to change the time.")
print("Time format: HH:MM:SS\n")

try:
    datetime.strptime(alarm_time, "%H:%M:%S")
except:
    print("❌ Wrong format inside CSV! Use HH:MM:SS")
    exit()

print("Press Ctrl + C to stop\n")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"\r🕒 Current Time: {now}", end="")

    if now == alarm_time:
        print("\n\n⏰ WAKE UP! ALARM RINGING!")
        play_sound()
        break

    time.sleep(1)
