import random

def main():
    """Main Number Guessing Game"""
    number = random.randint(1, 100)
    attempts = 0
   
    print("🎮 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
           
            if guess < number:
                print("📉 Too low! Try a bigger number.")
            elif guess > number:
                print("📈 Too high! Try a smaller number.")
            else:
                print(f"🎉 Correct! You guessed the number {number} in {attempts} attempts!")
                break
               
        except ValueError:
            print("❌ Please enter a valid integer only!")

if __name__ == "__main__":
    main()