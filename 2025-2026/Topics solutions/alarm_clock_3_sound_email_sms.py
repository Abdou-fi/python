# Build an alarm clock where users can set a specific time for the alarm to go off.
# The program will continuously check the current time and trigger the alarm when the set time is reached.
# The program should be able to handle different time formats and should be able to run indefinitely until the user manually stops it.
# The program should also be able to handle different time zones and should be able to handle different types of alarms such as sound alarms, text message alarms, and email alarms.
# The program should also be able to handle different types of alarms such as sound alarms, text message alarms, and email alarms.

import time
from datetime import datetime
import winsound  # For sound alarm on Windows  
import smtplib  # For email alarm
import requests  # For text message alarm

def set_alarm(alarm_time, alarm_type):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            trigger_alarm(alarm_type)
            break
        time.sleep(30)  # Check every 30 seconds
def trigger_alarm(alarm_type):
    if alarm_type == "sound":
        trigger_sound_alarm()

    elif alarm_type == "email":
        trigger_email_alarm()
def trigger_sound_alarm():
    winsound.Beep(1000, 2000)  # Frequency, Duration

    
def trigger_email_alarm():
    sender_email = "filalia@gmail.com"
    sender_password = "yourpassword"
    receiver_email = "fa0502@gmail.com"
    subject = "Alarm Notification"
    message = "Alarm! Time to wake up!"
    email_message = f"Subject: {subject}\n\n{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_message)
alarm_time = input("Enter the alarm time (HH:MM in 24-hour format): ")
alarm_type = input("Enter the alarm type (sound/text/email): ").lower()
alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, alarm_type))
alarm_thread.start()
alarm_thread.join()
""   
# Note: Replace placeholders in the trigger_text_alarm and trigger_email_alarm functions with actual credentials and phone numbers.
# Also, make sure to install the required libraries (winsound, smtplib, requests) before running the code.
# Note: This code is just an example and may not work as expected without proper configuration and credentials.
sender_email = ""
sender_password = ""
receiver_email = "" 
subject = "Alarm Notification"
message = "Alarm! Time to wake up!"
email_message = f"Subject: {subject}\n\n{message}"
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, email_message)
# Note: Replace placeholders in the trigger_text_alarm and trigger_email_alarm functions with actual credentials and phone numbers.
# Also, make sure to install the required libraries (winsound, smtplib, requests) before running the code.
# Note: This code is just an example and may not work as expected without proper configuration and credentials.

