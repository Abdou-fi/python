import random
import string

def get_user_preferences():
    """Get password generation preferences from user"""
    print("🔐 Password Generator")
    print("=" * 30)
   
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length must be positive")
    except ValueError:
        print("❌ Invalid length. Using default: 12")
        length = 12
   
    use_letters = input("Include letters? (y/n): ").lower().startswith('y')
    use_numbers = input("Include numbers? (y/n): ").lower().startswith('y')
    use_symbols = input("Include symbols? (y/n): ").lower().startswith('y')
   
    return length, use_letters, use_numbers, use_symbols

def generate_character_set(use_letters, use_numbers, use_symbols):
    """Build character set based on user preferences"""
    characters = ""
   
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
   
    return characters

def generate_password(length, characters):
    """Generate secure random password"""
    if not characters:
        raise ValueError("No character types selected!")
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main password generator function"""
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
   
    characters = generate_character_set(use_letters, use_numbers, use_symbols)
   
    try:
        password = generate_password(length, characters)
        print(f"✅ Generated Password: {password}")
        print(f"📊 Length: {length} | Characters: {len(characters)} types")
        print("💡 Tip: Store this securely!")
       
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("Please select at least one character type.")

if __name__ == "__main__":
    main()