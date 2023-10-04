# This program is contributed by Gaurav Mandal 


import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True, use_salt=False, memorable=False):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation

    # Create a character set based on options
    character_set = ""
    if use_lowercase:
        character_set += lowercase_chars
    if use_uppercase:
        character_set += uppercase_chars
    if use_digits:
        character_set += digit_chars
    if use_special_chars:
        character_set += special_chars

    if not (use_lowercase or use_uppercase or use_digits or use_special_chars):
        raise ValueError("At least one character set (lowercase, uppercase, digits, special chars) must be selected.")

    # Generate a memorable password
    if memorable:
        memorable_password = ""
        vowels = "aeiou"
        consonants = "".join(set(lowercase_chars) - set(vowels))

        for _ in range(length):
            if _ % 2 == 0:
                memorable_password += random.choice(consonants)
            else:
                memorable_password += random.choice(vowels)

        if use_uppercase:
            memorable_password = memorable_password.capitalize()

        return memorable_password

    # Generate a random password
    password = ''.join(random.choice(character_set) for _ in range(length))

    # Add salt to the password
    if use_salt:
        salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        password = salt + password

    return password

def main():
    length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    use_salt = input("Use salt? (yes/no): ").lower() == "yes"
    memorable = input("Generate memorable password? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, use_salt, memorable)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

# This code is contributed by Gaurav Mandall (https://www.linkedin.com/in/gauravmandall/)