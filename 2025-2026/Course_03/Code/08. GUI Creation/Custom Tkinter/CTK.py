import customtkinter as ctk
app = ctk.CTk()
app.geometry("300x250")
app.title("CustomTkinter Example")

def show_text():
    pass
    
label = ctk.CTkLabel(
    app, 
    text="Enter your name",
    font=("Arial", 16)
)
label.pack(pady=20)

entry = ctk.CTkEntry(
    app, 
    placeholder_text="Name"
)

entry.pack(pady=20)
button = ctk.CTkButton(
    app, 
    text="Submit", 
    command=show_text
)

button.pack(pady=20)

app.mainloop()