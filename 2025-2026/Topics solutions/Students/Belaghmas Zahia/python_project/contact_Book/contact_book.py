import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("دفتر العناوين - Contact Book")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
       
        self.contacts = {}
        self.setup_ui()
   
    def setup_ui(self):
        """إعداد عناصر الواجهة الرسومية"""

        self.listbox = tk.Listbox(
            self.root,
            width=60,
            height=15,
            font=("Arial", 10)
        )
        self.listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
       
        self.add_button = tk.Button(
            button_frame,
            text="إضافة جهة اتصال",
            width=18,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.add_contact
        )
        self.add_button.pack(side=tk.LEFT, padx=5)
       
        self.delete_button = tk.Button(
            button_frame,
            text="حذف جهة اتصال",
            width=18,
            height=2,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.delete_contact
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)
    
        self.refresh_button = tk.Button(
            button_frame,
            text="تحديث القائمة",
            width=18,
            height=2,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.update_list
        )
        self.refresh_button.pack(side=tk.LEFT, padx=5)
        self.update_list()
   
    def update_list(self):
        self.listbox.delete(0, tk.END)
        for name, phone in sorted(self.contacts.items()):
            self.listbox.insert(tk.END, f"{name:<20} | {phone}")
   
    def add_contact(self):
        name = simpledialog.askstring("إضافة جهة اتصال", "أدخل الاسم:")
        if not name or name.strip() == "":
            return
       
        phone = simpledialog.askstring("إضافة جهة اتصال", "أدخل رقم الهاتف:")
        if not phone or phone.strip() == "":
            return
       
        self.contacts[name.strip()] = phone.strip()
        messagebox.showinfo("تم", f"تم إضافة جهة الاتصال:{name}")
        self.update_list()
   
    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("تحذير", "يرجى اختيار جهة اتصال لحذفها.")
            return
       
        entry = self.listbox.get(selected[0])
        name = entry.split("|")[0].strip()
       
        if messagebox.askyesno("تأكيد الحذف", f"هل تريد حذف جهة الاتصال:{name}؟"):
            del self.contacts[name]
            messagebox.showinfo("تم", f"تم حذف جهة الاتصال: {name}")
            self.update_list()

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()