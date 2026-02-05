import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6)) 
x = np.linspace(0, 2 * np.pi, 100) 
line1, = ax1.plot(x, np.sin(x), 'r-')  # Red sine wave 
line2, = ax2.plot(x, np.cos(x), 'b-') # Blue cosine wave 
    
# Function to update the animation 
def update(frame): 
    line1.set_ydata(np.sin(x + frame / 10.0))
    line2.set_ydata(np.cos(x + frame / 10.0)) 
    return line1, line2 
    
# Create the animation object 
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True) 
    
# Show the animation 
plt.show()