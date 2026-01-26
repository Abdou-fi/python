import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = None  # Can be set later
   
    def get_user_guess(self):
        """Get valid guess from user"""
        while True:
            try:
                guess = input("Enter your guess (1-100): ").strip()
                if not guess.isdigit():
                    print("❌ Please enter a valid integer")
                    continue
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("❌ Please enter a number between 1 and 100")
                    continue
                return guess
            except ValueError:
                print("❌ Input error, try again")
   
    def play(self):
        """Main game loop"""
        print("🎯 Welcome to Number Guessing Game!")
        print("Computer has chosen a random number between 1 and 100")
        print("Try to guess it in fewest attempts!")
        while True:
            guess = self.get_user_guess()
            self.attempts += 1
           
            if guess < self.secret_number:
                print("📈 Too low! Try a bigger number")
            elif guess > self.secret_number:
                print("📉 Too high! Try a smaller number")
            else:
                print(f" Congratulations! Correct!")
                print(f"You guessed it in {self.attempts} attempts!")
                break

    def run(self):
        """Run the game"""
        try:
            self.play()
        except KeyboardInterrupt:
            print("👋 Game stopped. Goodbye!")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()