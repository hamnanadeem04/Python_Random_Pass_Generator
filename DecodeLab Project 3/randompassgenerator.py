import random
import string

print("===== MY PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits

characters = letters + numbers

password = ""

for i in range(length):
    character = random.choice(characters)
    password = password + character

print("\nYour Generated Password:", password)