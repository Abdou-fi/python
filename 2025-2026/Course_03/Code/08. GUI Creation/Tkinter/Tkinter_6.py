
#  create a tkinter window with 3 labels, 2 entry and button to concatenate the text in the entry fields and display it in the label
from myfunctions import arabic_display
import tkinter as tk

window = tk.Tk()
window.title('مرحباً بك في تطبيق Tkinter')
window.geometry('600x500')

label1 = tk.Label(window, text='أدخل اسمك')
label1.config(font=('Amiri', 20))
label1.pack()

entry1 = tk.Entry(window)
entry1.config(font=('Amiri', 20))
entry1.pack()

label2 = tk.Label(window, text=arabic_display('ادخل عمرك:'), fg="blue", font=("Amiri", 22), padx=10, pady=10)
label2.pack()

entry2 = tk.Entry(window)
entry2.config(font=('Amiri', 20))
entry2.pack()

def concatenate():
    name = entry1.get()
    age = entry2.get()
    result_label.config(text= arabic_display(f'مرحبا بك {name} عمرك {age} سنة.'))

button = tk.Button(window, text='Concatenate', command=concatenate)
button.config(font=('Arial', 16))
button.pack()
result_label = tk.Label(window, text='')
result_label.config(font=('Amiri', 30))
result_label.pack()

window.mainloop()
