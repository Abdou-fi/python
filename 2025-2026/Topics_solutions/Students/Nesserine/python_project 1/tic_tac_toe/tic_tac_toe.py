import tkinter as tk
from tkinter import messagebox, ttk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Tic-Tac-Toe")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
       
        self.current_player = "X"
        self.buttons = [[None] * 3 for _ in range(3)]
        self.game_active = True
       
        self.setup_ui()
   
    def setup_ui(self):
        title_frame = ttk.Frame(self.root, padding="20")
        title_frame.pack(fill=tk.X)
       
        ttk.Label(title_frame, text="Tic-Tac-Toe",
                 font=("Arial", 20, "bold")).pack(pady=(0, 10))
       
        self.turn_label = ttk.Label(title_frame, text="X's Turn",
                                   font=("Arial", 12))
        self.turn_label.pack()
       
        board_frame = ttk.Frame(self.root, padding="20")
        board_frame.pack(expand=True)
       
        for i in range(3):
            for j in range(3):
                btn = tk.Button(board_frame, text="", width=8, height=3,
                               font=("Arial", 24, "bold"),
                               bg="#f8f9fa", fg="#495057",
                               relief="flat", bd=2,
                               command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
       
        control_frame = ttk.Frame(self.root, padding="20")
        control_frame.pack(fill=tk.X)
       
        ttk.Button(control_frame, text="🔄 New Game",
                  command=self.reset_game).pack(side=tk.LEFT)
        ttk.Button(control_frame, text="🚪 Exit",
                  command=self.root.quit).pack(side=tk.RIGHT)
   
    def on_click(self, row, col):

        if (self.game_active and self.buttons[row][col]["text"] == ""):
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col].config(bg="#28a745" if self.current_player == "X"
                                        else "#007bff")
           
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("🏆 Winner!", f"Player {winner} wins!")
                self.game_active = False
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a Tie! 🤝")
                self.game_active = False
            else:
                self.switch_player()
   
    def check_winner(self):
        for i in range(3):
            if (self.buttons[i][0]["text"] == self.buttons[i][1]["text"] ==
                self.buttons[i][2]["text"] != ""):
                return self.buttons[i][0]["text"]
            if (self.buttons[0][i]["text"] == self.buttons[1][i]["text"] ==
                self.buttons[2][i]["text"] != ""):
                return self.buttons[0][i]["text"]
       
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] ==
            self.buttons[2][2]["text"] != ""):
            return self.buttons[0][0]["text"]
        if (self.buttons[0][2]["text"] == self.buttons[1][1]["text"] ==
            self.buttons[2][0]["text"] != ""):
            return self.buttons[0][2]["text"]
       
        return None
   
    def is_board_full(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
   
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(text=f"{self.current_player}'s Turn")
   
    def reset_game(self):
        self.current_player = "X"
        self.game_active = True
        self.turn_label.config(text="X's Turn")
       
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg="#f8f9fa")

def main():
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()