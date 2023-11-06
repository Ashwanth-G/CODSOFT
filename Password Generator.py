import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print('''----------------------------------------------------------------------
----------------- Welcome to the Password Generator! -----------------
----------------------------------------------------------------------''')
    try:
        length = int(input("\n\nEnter the desired password length: "))
        if length <= 0:
            print("Password length should be a positive integer.")
            return

        include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, include_digits, include_special_chars)

        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid password length as a positive integer.")

if __name__ == "__main__":
    main()
  
