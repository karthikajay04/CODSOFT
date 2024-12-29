import random
import string
num = int(input("Enter the length of password:"))
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
symbols = string.punctuation
all_characters = uppercase_letters + lowercase_letters +  symbols
password = ''.join(random.choice(all_characters) for _ in range(num))
print("Generated Password:", password)
