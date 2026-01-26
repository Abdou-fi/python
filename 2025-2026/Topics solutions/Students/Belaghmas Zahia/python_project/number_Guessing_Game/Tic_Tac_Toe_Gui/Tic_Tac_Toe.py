import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
       
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_active = True
       
        self.setup_ui()
   
    def check_winner(self):
        """Check rows, columns, and diagonals for winner"""
        # Check rows
        for i in range(3):
            if (self.buttons[i][0]["text"] == self.buttons[i][1]["text"] ==
                self.buttons[i][2]["text"] != ""):
                return self.buttons[i][0]["text"]
       
        # Check columns
        for i in range(3):
            if (self.buttons[0][i]["text"] == self.buttons[1][i]["text"] ==
                self.buttons[2][i]["text"] != ""):
                return self.buttons[0][i]["text"]
       
        # Check diagonals
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] ==
            self.buttons[2][2]["text"] != ""):
            return self.buttons[0][0]["text"]
       
        if (self.buttons[0][2]["text"] == self.buttons[1][1]["text"] ==
            self.buttons[2][0]["text"] != ""):
            return self.buttons[0][2]["text"]
       
        # Check for draw
        if all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            return "Draw"
       
        return None
   
    def on_click(self, row, col):
        """Handle button click"""
        if (not self.game_active or
            self.buttons[row][col]["text"] != ""):
            return
       
        # Place current player's mark
        self.buttons[row][col]["text"] = self.current_player
       
        # Check for winner
        result = self.check_winner()
        if result:
            self.end_game(result)
            return
       
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
   
    def end_game(self, result):
        """Show game over message and reset"""
        self.game_active = False
        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {result} wins!")
        self.reset_board()
   
    def reset_board(self):
        """Reset game to initial state"""
        self.current_player = "X"
        self.game_active = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
   
    def setup_ui(self):
        """Create and arrange all UI elements"""
        # Title label
        title = tk.Label(self.root, text="Tic Tac Toe",
                        font=("Arial", 24, "bold"))
        title.pack(pady=10)
       
        # Status label
        self.status_label = tk.Label(self.root, text="Player X's turn",
                                   font=("Arial", 16))
        self.status_label.pack(pady=5)
       
        # Game board frame
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=20)
       
        # Create buttons
        for i in range(3):
            for j in range(3):
                btn = tk.Button(board_frame, text="", width=6, height=3,
                              font=("Arial", 24, "bold"),
                              command=lambda r=i, c=j: self.on_click(r, c),
                              bg="#f0f0f0", relief="raised")
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
       
        # Reset button
        reset_btn = tk.Button(self.root, text="New Game",
                            width=12, height=2, font=("Arial", 14),
                            command=self.reset_board, bg="#4CAF50",
                            fg="white")
        reset_btn.pack(pady=20)
   
    def run(self):
        """Start the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
