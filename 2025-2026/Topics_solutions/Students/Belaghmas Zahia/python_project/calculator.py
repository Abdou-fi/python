import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
       
        self.expression = ""
       
        self.setup_ui()
   
    def press(self, value):
        self.expression += str(value)
        self.entry_text.set(self.expression)
   
    def equal(self):
        try:
            result = str(eval(self.expression))
            self.entry_text.set(result)
            self.expression = result
        except:
            self.entry_text.set("Error")
            self.expression = ""
   
    def clear(self):
        self.expression = ""
        self.entry_text.set("")
   
    def setup_ui(self):
        self.entry_text = tk.StringVar()
        entry = tk.Entry(
            self.window,
            textvariable=self.entry_text,
            font=("Arial", 20),
            bd=10,
            relief="sunken",
            justify="right"
        )
        entry.pack(fill="both", ipadx=8, ipady=15)
       
        frame = tk.Frame(self.window)
        frame.pack()
       
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
       
        for text, row, col in buttons:
            if text == '=':
                btn = tk.Button(
                    frame,
                    text=text,
                    width=5,
                    height=2,
                    font=("Arial", 14),
                    command=self.equal
                )
            else:
                btn = tk.Button(
                    frame,
                    text=text,
                    width=5,
                    height=2,
                    font=("Arial", 14),
                    command=lambda t=text: self.press(t)
                )
            btn.grid(row=row, column=col, padx=5, pady=5)
       
        clear_btn = tk.Button(
            self.window,
            text="Clear",
            width=22,
            height=2,
            font=("Arial", 14),
            command=self.clear
        )
        clear_btn.pack(pady=10)
   
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()