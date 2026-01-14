# using time module tricks
import time

def get_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    return formatted_time

print(get_time())
time.sleep(3)
print(get_time())
print(time.timezone) # to get the timezone difference in seconds west of UTC