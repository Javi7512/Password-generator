import random
import string

def generate_password(length):
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = lowercase + uppercase + digits + special_characters
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (8 - 32): "))
            if 8 <= length <= 32:
                break
            else:
                print("Please enter a length between 8 and 32.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
