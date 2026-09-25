# Python Random Password Generator

A simple Python-based Password Generator that asks the user for a desired password length and generates a random password using letters and numbers.

## Features

* User can choose the password length.
* Generates passwords using uppercase and lowercase letters.
* Includes numbers from 0 to 9.
* Uses Python's `random` module to select characters randomly.
* Beginner-friendly Python project.

## Technologies Used

* Python
* random module
* string module

## How It Works

1. The program asks the user to enter the desired password length.
2. It gets uppercase and lowercase letters using `string.ascii_letters`.
3. It gets numbers using `string.digits`.
4. Letters and numbers are combined into one character set.
5. `random.choice()` selects random characters.
6. The selected characters are added until the requested password length is reached.
7. The generated password is displayed on the screen.

## Code

```python
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
```

## Example Output

```text
===== MY PASSWORD GENERATOR =====
Enter password length: 8

Your Generated Password: aG7kP29m
```

The output will be different each time because the characters are selected randomly.

## Concepts Practiced

This project helped me practice:

* Importing Python modules
* `random.choice()`
* String manipulation
* `input()`
* Type conversion using `int()`
* Variables
* `for` loops
* `range()`
* String concatenation
## Clone Repository

To clone this repository to your local computer, run:

git clone https://github.com/hamnanadeem04/Python_Random_Pass_Generator.git
## How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file named:

```text
password_generator.py
```

3. Open the terminal in the project folder.
4. Run the following command:

```bash
python password_generator.py
```

5. Enter the desired password length.

## Project Purpose

This project was created as a beginner Python exercise to practice importing modules, loops, random selection, and string manipulation while building a simple password generator.
## Author
Hamna Khan
Computer Science Student| Aspiring AI/ML Developer
