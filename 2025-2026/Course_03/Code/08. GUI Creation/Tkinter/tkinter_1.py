import tkinter as tk

print('tkinter is available')
print('Standard GUI toolkit for Python')


# Create a window
window = tk.Tk()

# Set the title of the window
window.title('My First GUI')

# Set the size of the window
window.geometry('400x300')

# Create a label
label = tk.Label(window, text='Hello, World!')

# Pack the label into the window
label.pack()

# Start the main loop
window.mainloop()
print('GUI window has been closed')
print('End of tkinter example')
# End of the program