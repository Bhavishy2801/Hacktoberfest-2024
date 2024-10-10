import random
import string

# Function to generate a password
def generate_password(length):
    # Define the character set: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Generate the rest of the password
    password += random.choices(characters, k=length - 4)

    # Shuffle the resulting password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Main function
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length (minimum 8): "))

    # Ensure the password is at least 8 characters long
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

# Run the program
main()
