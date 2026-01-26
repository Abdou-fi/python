import tkinter as tk
from tkinter import messagebox, ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("💱 Currency Converter Pro")
        self.root.geometry("450x500")
        self.root.resizable(True, True)
       
        self.default_rates = {"USD_EUR": 0.92, "USD_DZD": 134.50}
       
        self.setup_ui()
        self.load_default_rates()
   
    def setup_ui(self):
        title_label = ttk.Label(self.root, text="Currency Converter",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
       
        rate_frame = ttk.LabelFrame(self.root, text="Exchange Rates", padding=10)
        rate_frame.pack(fill=tk.X, padx=20, pady=5)
       
        ttk.Label(rate_frame, text="USD → EUR:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_usd_eur = ttk.Entry(rate_frame, width=15)
        self.entry_usd_eur.grid(row=0, column=1, padx=5, pady=2)
       
        ttk.Label(rate_frame, text="USD → DZD:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_usd_dzd = ttk.Entry(rate_frame, width=15)
        self.entry_usd_dzd.grid(row=1, column=1, padx=5, pady=2)
       
        ttk.Button(rate_frame, text="Default Rates",
                  command=self.load_default_rates).grid(row=0, column=2, rowspan=2, padx=10)
       
        convert_frame = ttk.LabelFrame(self.root, text="Conversion", padding=10)
        convert_frame.pack(fill=tk.X, padx=20, pady=10)
       
        ttk.Label(convert_frame, text="Amount:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_amount = ttk.Entry(convert_frame, width=20, font=("Arial", 12))
        self.entry_amount.grid(row=0, column=1, padx=5, pady=5)
        self.entry_amount.bind('<Return>', lambda e: self.convert())
       
        ttk.Label(convert_frame, text="From → To:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.var = tk.StringVar(value="USD to EUR")
        self.option_menu = ttk.Combobox(convert_frame, textvariable=self.var,
                                       values=["USD to EUR", "USD to DZD",
                                              "EUR to USD", "DZD to USD"],
                                       state="readonly", width=17)
        self.option_menu.grid(row=1, column=1, padx=5, pady=5)
       
        ttk.Button(convert_frame, text="🔄 Convert",
                  command=self.convert).grid(row=2, column=0, columnspan=2, pady=10)
       
        self.result_frame = ttk.LabelFrame(self.root, text="Result", padding=15)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
       
        self.label_result = ttk.Label(self.result_frame,
                                    text="Enter values and click Convert",
                                    font=("Arial", 14))
        self.label_result.pack(expand=True)
       
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
   
    def load_default_rates(self):
        self.entry_usd_eur.delete(0, tk.END)
        self.entry_usd_eur.insert(0, str(self.default_rates["USD_EUR"]))
       
        self.entry_usd_dzd.delete(0, tk.END)
        self.entry_usd_dzd.insert(0, str(self.default_rates["USD_DZD"]))
       
        self.status_var.set("Default rates loaded")
   
    def convert(self):
        try:
            usd_to_eur = float(self.entry_usd_eur.get())
            usd_to_dzd = float(self.entry_usd_dzd.get())
            amount = float(self.entry_amount.get())
           
            if amount <= 0:
                raise ValueError("Amount must be positive")
           
            option = self.var.get()
           
            if option == "USD to EUR":
                result = amount * usd_to_eur
                display = f"{amount:.2f} USD → {result:.2f} EUR"
            elif option == "USD to DZD":
                result = amount * usd_to_dzd
                display = f"{amount:.2f} USD → {result:.2f} DZD"
            elif option == "EUR to USD":
                result = amount / usd_to_eur
                display = f"{amount:.2f} EUR → {result:.2f} USD"
            elif option == "DZD to USD":
                result = amount / usd_to_dzd
                display = f"{amount:.2f} DZD → {result:.2f} USD"
            else:
                raise ValueError("Invalid option")
           
            self.label_result.config(text=display, foreground="green")
            self.status_var.set(f"Converted: {display}")
           
        except ValueError as e:
            error_msg = str(e) if "Amount" in str(e) else "Invalid input numbers!"
            messagebox.showerror("Conversion Error", error_msg)
            self.label_result.config(text="Conversion failed", foreground="red")
            self.status_var.set("Error occurred")

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()