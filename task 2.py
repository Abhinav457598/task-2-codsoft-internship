# -----------------------------------------------
# Name     : [Abhinav Pal]
# Project  : Advanced Password Generator in Python
# Role     : Intern @ CodSoft
# Description:
#   This script allows users to generate a random password
#   based on their preferred length and character complexity.
#   Developed as part of my internship experience at CodSoft.
# -----------------------------------------------

import random
import string

print(" Welcome to the Password Generator!")

# Get password length from user
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password should be at least 4 characters long for better strength.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

print("\nChoose the complexity of your password:")
print("1. Only letters (A–Z, a–z)")
print("2. Letters and numbers")
print("3. Letters, numbers, and symbols")

complexity_choice = input("Enter your choice (1/2/3): ")

if complexity_choice == '1':
    characters = string.ascii_letters
elif complexity_choice == '2':
    characters = string.ascii_letters + string.digits
elif complexity_choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    exit()

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the result
print("\nYour generated password is:")
print(password)
