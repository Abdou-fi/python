import secrets
import string
import tkinter as tk

def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(int(length_entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, password)
    
def copy_to_clipboard(): 
    root.clipboard_clear() 
    root.clipboard_append(entry.get())

root = tk.Tk()
root.geometry("400x250")
root.title("Secure password generator")

length_label = tk.Label( text="Enter the length of the password:", font=("Arial", 14), justify='center')
length_label.pack()

length_entry = tk.Entry(font=("Arial", 18), justify='center')
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password",font=("Arial", 14), justify='center' ,command=generate_password)
generate_button.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18), justify='center')
entry.pack()

copy_button = tk.Button(root, text="Copy",font=("Arial", 14), justify='center' , command=copy_to_clipboard)
copy_button.pack(pady=20)

root.mainloop()

    
    