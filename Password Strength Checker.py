import re

# Define the criteria for a strong password
min_length = 8
regex_uppercase = re.compile(r'[A-Z]')
regex_lowercase = re.compile(r'[a-z]')
regex_digit = re.compile(r'\d')
regex_symbol = re.compile(r'[!@#$%^&*()\-_=+{}[\]|;:",<.>/?]')

# Prompt the user for a password
password = input("Enter a password: ")

# Check the password strength
length_ok = len(password) >= min_length
uppercase_ok = regex_uppercase.search(password) is not None
lowercase_ok = regex_lowercase.search(password) is not None
digit_ok = regex_digit.search(password) is not None
symbol_ok = regex_symbol.search(password) is not None

# Provide feedback on password strength
if length_ok and uppercase_ok and lowercase_ok and digit_ok and symbol_ok:
    print("Your password is strong!")
else:
    print("Your password could be stronger - try adding more symbols or numbers.")
