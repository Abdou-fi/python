from cProfile import label
import tkinter as tk

# Create a window with title and size

window = tk.Tk()
window.title('My First GUI')
window.geometry('400x300')

# create a temperature converter from Celsius to Fahrenheit

def convert():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    label.config(text=f'{fahrenheit}°F')
   

label = tk.Label(window, text='Enter temperature in Celsius')
label.config(font=('Arial', 20))
label.pack()

entry = tk.Entry(window)
entry.config(font=('Arial', 20))
entry.pack()

button = tk.Button(window, text='Convert', command=convert)
button.config(font=('Arial', 20))
button.pack()

window.mainloop()