#  create a tkinter window with 3 labels, 2 entry and button to concatenate the text in the entry fields and display it in the label

import tkinter as tk

window = tk.Tk()
window.title('تطبيقي الأول باستخدام Tkinter')
window.geometry('600x500')

label1 = tk.Label(window, text='أدخل اسمك')
label1.config(font=('Arial', 20))
label1.pack()

entry1 = tk.Entry(window)
entry1.config(font=('Arial', 20))
entry1.pack()

label2 = tk.Label(window, text='ادخل عمرك:', fg="blue", font=("Arial", 14), padx=10, pady=10)
label2.config(font=('Arial', 20))
label2.pack()

entry2 = tk.Entry(window)
entry2.config(font=('Arial', 20))
entry2.pack()

def concatenate():
    name = entry1.get()
    age = entry2.get()
    result_label.config(text=f'مرحبا بك  {name} عمرك {age} سنة')

button = tk.Button(window, text='Concatenate', command=concatenate)
button.config(font=('Arial', 16))
button.pack()
result_label = tk.Label(window, text='')
result_label.config(font=('Times New Roman', 30))
result_label.pack()

window.mainloop()
