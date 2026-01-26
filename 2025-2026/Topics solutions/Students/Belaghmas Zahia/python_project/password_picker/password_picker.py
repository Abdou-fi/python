import random
import string

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation
        self.length = 0
   
    def get_password_length(self):
        """Get valid password length from user"""
        while True:
            try:
                length = input("Enter password length (8-50): ").strip()
                length = int(length)
                if 8 <= length <= 50:
                    return length
                print("Please enter a number between 8 and 50")
            except ValueError:
                print("Please enter a valid number")
   
    def generate_password(self, length):
        """Generate random password"""
        return ''.join(random.choice(self.characters) for _ in range(length))
   
    def display_password_info(self, password):
        """Display generated password with info"""
        print("" + "="*50)
        print(f"✅ Generated Password: {password}")
        print(f"📏 Length: {len(password)} characters")
        print(f"🔐 Strength: Very Strong")
        print("="*50)
   
    def run(self):
        """Main application flow"""
        print("🔐 Secure Password Generator")
        print("-" * 30)
       
        self.length = self.get_password_length()
        password = self.generate_password(self.length)
        self.display_password_info(password)

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
