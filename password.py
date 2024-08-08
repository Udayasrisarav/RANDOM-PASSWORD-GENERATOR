import string
import random

def generate_password(length, include_letters, include_numbers, include_symbols):
    char_set = ''
    
    if include_letters:
        char_set += string.ascii_letters
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation
    
    if not char_set:
        raise ValueError("No character types selected for password generation.")
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        
        include_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
