import tkinter as tk
def button_clicked():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "Button clicked!")

window = tk.Tk()

button = tk.Button(window, text='Click me!', command=button_clicked)
button.pack()

entry = tk.Entry(window)
entry.pack()

window.mainloop()