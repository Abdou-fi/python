import tkinter as tk

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

#  Create a button
def on_button_click():
    label.config(text='Button Clicked!')

button = tk.Button(window, text='Click Me', command=on_button_click)

# Pack the button into the window
button.pack()


# Start the main loop
window.mainloop()
