import numpy as np
# temperature in degrees celsius for 7 days
temps=np.array([29.3, 42.1, 18.8, 22.1, 17.6, 28.7, 33.4])
#average temperature
avg_temp=np.mean(temps)
print(f"Average temperature for 7 days: {avg_temp:.2f} degrees celsius")
#highest temperature
max_temp=np.max(temps)
print(f"Highest temperature for 7 days: {max_temp:.2f} degrees celsius")
#lowest temperature
min_temp=np.min(temps)
print(f"Lowest temperature for 7 days: {min_temp:.1f} degrees celsius")