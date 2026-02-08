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
    label2.config(text=f'{celsius}°C = {fahrenheit}°F')
   

label1 = tk.Label(window, text='Temperature in Celsius degrees:')
label1.config(font=('Arial', 16))
label1.pack()

entry = tk.Entry(window)
entry.config(font=('Arial', 20))
entry.pack()

button = tk.Button(window, text='Convert', command=convert)
button.config(font=('Arial', 20))
button.pack()

label2 = tk.Label(window, text=' ')
label2.config(font=('Arial', 20))
label2.pack()

window.mainloop()