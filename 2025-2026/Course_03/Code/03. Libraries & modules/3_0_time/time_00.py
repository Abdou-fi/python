# using time module to get current time and format it
import time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("Current Time:", formatted_time)
# pause execution for 2 seconds
time.sleep(2)
print("2 seconds have passed")
# get the current epoch time
epoch_time = time.time()
print("Epoch Time:", epoch_time)
# convert epoch time back to local time
local_time = time.localtime(epoch_time)
print("Converted Local Time:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))