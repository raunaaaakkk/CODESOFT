import random
import string

def generate_password(length):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the created password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()