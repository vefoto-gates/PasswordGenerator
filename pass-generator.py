import random
import string

class PasswordGenerator:
    def __init__(self):
        self.char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    def generate_password(self, length=12, use_special_chars=True, memorable=False):
        if length < 8 or length > 16:
            return "Enter a suitable password length (between 8 and 16)."

        password = ''.join(random.choice(self.char_seq) for _ in range(length))

        if memorable:
            vowels = "aeiou"
            consonants = "".join(set(self.char_seq.lower()) - set(vowels))

            memorable_password = ""
            for i in range(length):
                if i % 2 == 0:
                    memorable_password += random.choice(consonants)
                else:
                    memorable_password += random.choice(vowels)

            return memorable_password

        if use_special_chars:
            password += random.choice(string.punctuation)

        password_list = list(password)
        random.shuffle(password_list)
        final_password = ''.join(password_list)

        return final_password

def main():
    print("Enter the required length of the password ranging from 8 to 16:")
    length = int(input())

    generator = PasswordGenerator()
    password = generator.generate_password(length, use_special_chars=True, memorable=True)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
