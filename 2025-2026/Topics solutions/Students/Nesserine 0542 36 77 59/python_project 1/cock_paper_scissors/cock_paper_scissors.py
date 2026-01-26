import tkinter as tk
from tkinter import messagebox, ttk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock, Paper, Scissors Pro")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
       
        # إحصائيات اللعبة
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
       
        # خيارات اللعبة
        self.choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
       
        self.setup_ui()
   
    def setup_ui(self):
        """إعداد الواجهة الرسومية"""
        # العنوان الرئيسي
        title_frame = ttk.Frame(self.root, padding=20)
        title_frame.pack(fill=tk.X)
       
        ttk.Label(title_frame, text="Rock, Paper, Scissors",
                 font=("Arial", 20, "bold")).pack()
        ttk.Label(title_frame, text="Choose your move!",
                 font=("Arial", 10)).pack(pady=(0, 20))
       
        # إحصائيات اللعبة
        stats_frame = ttk.LabelFrame(self.root, text="Score", padding=10)
        stats_frame.pack(fill=tk.X, padx=20, pady=5)
       
        self.player_label = ttk.Label(stats_frame, text="You: 0",
                                     font=("Arial", 12, "bold"))
        self.player_label.grid(row=0, column=0, padx=10)
       
        self.ties_label = ttk.Label(stats_frame, text="Ties: 0")
        self.ties_label.grid(row=0, column=1, padx=10)
       
        self.computer_label = ttk.Label(stats_frame, text="Computer: 0",
                                       font=("Arial", 12, "bold"))
        self.computer_label.grid(row=0, column=2, padx=10)
       
        # منطقة اللعب
        game_frame = ttk.Frame(self.root, padding=20)
        game_frame.pack(expand=True)
       
        # اختيارات اللاعب
        self.player_choice_label = ttk.Label(game_frame, text="Your choice: ?",
                                           font=("Arial", 14))
        self.player_choice_label.pack(pady=10)
       
        buttons_frame = ttk.Frame(game_frame)
        buttons_frame.pack(pady=20)
       
        for i, choice in enumerate(self.choices):
            btn = ttk.Button(buttons_frame, text=choice,
                           command=lambda c=choice: self.play(c),
                           width=12)
            btn.pack(pady=5, fill=tk.X)
       
        # اختيار الكمبيوتر
        self.computer_choice_label = ttk.Label(game_frame, text="Computer: ?",
                                             font=("Arial", 14))
        self.computer_choice_label.pack(pady=10)
       
        # النتيجة
        self.result_label = ttk.Label(game_frame, text="",
                                    font=("Arial", 16, "bold"),
                                    foreground="blue")
        self.result_label.pack(pady=20)
       
        # أزرار التحكم
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=20, pady=10)
       
        ttk.Button(control_frame, text="🔄 Reset Score",
                  command=self.reset_game).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="❓ Rules",
                  command=self.show_rules).pack(side=tk.RIGHT, padx=5)
       
        # شريط الحالة
        self.status_var = tk.StringVar(value="Ready to play!")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
   
    def play(self, player_choice):
        """لعب جولة واحدة"""
        computer_choice = random.choice(self.choices)
       
        # عرض الاختيارات
        self.player_choice_label.config(text=f"You: {player_choice}")
        self.computer_choice_label.config(text=f"Computer: {computer_choice}")
       
        # تحديد الفائز
        result = self.determine_winner(player_choice, computer_choice)
       
        # تحديث النتيجة والإحصائيات
        self.update_result(result)
        self.update_stats(result)
       
        self.status_var.set(f"Round finished! {result}")
   
    def determine_winner(self, player, computer):
        """تحديد الفائز في الجولة"""
        player_text = player.replace("🪨 ", "").replace("📄 ", "").replace("✂️ ", "")
        computer_text = computer.replace("🪨 ", "").replace("📄 ", "").replace("✂️ ", "")
       
        if player_text == computer_text:
            return "It's a tie! 🤝"
        elif (
            (player_text == "Rock" and computer_text == "Scissors") or
            (player_text == "Paper" and computer_text == "Rock") or
            (player_text == "Scissors" and computer_text == "Paper")
        ):
            return "🎉 You win!"
        else:
            return "🤖 Computer wins!"
   
    def update_result(self, result):
        """تحديث عرض النتيجة"""
        self.result_label.config(text=result)
       
        if "You win" in result:
            self.result_label.config(foreground="green")
        elif "Computer wins" in result:
            self.result_label.config(foreground="red")
        else:
            self.result_label.config(foreground="orange")
   
    def update_stats(self, result):
        """تحديث الإحصائيات"""
        if "You win" in result:
            self.player_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1
        else:
            self.ties += 1
       
        self.player_label.config(text=f"You: {self.player_score}")
        self.computer_label.config(text=f"Computer: {self.computer_score}")
        self.ties_label.config(text=f"Ties: {self.ties}")
   
    def reset_game(self):
        """إعادة تعيين اللعبة"""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
       
        self.player_choice_label.config(text="Your choice: ?")
        self.computer_choice_label.config(text="Computer: ?")
        self.result_label.config(text="")
       
        self.update_stats("reset")
        self.status_var.set("Game reset!")
   
    def show_rules(self):
        rules = """Rules:
• Rock beats Scissors ✂️🪨
• Paper beats Rock 📄🪨 
• Scissors beats Paper ✂️📄
• Same choices = Tie 🤝"""
        messagebox.showinfo("Game Rules", rules)

def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()