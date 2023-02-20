
from pikepdf import *
from tqdm import tqdm

# Create an empty password list
passwords = []

# Text File Containing all the passwords (12.647)
password_text_file = "passwords.txt"

# Iterate the loop through each line
# and store in passwords list
for line in open(password_text_file, errors="ignore"):
    passwords.append(line.strip())

# iterate over passwords
for password in tqdm(passwords, "Cracking PDF File"):
    try:
        # open PDF file and check each password
        with pikepdf.open("tocrack.pdf",
            password = password) as p:
            # If password is correct, break the loop
            print("[+] You found the password:", password)
        break
    # If the password does not match, it will raise PasswordError
    except pikepdf.PasswordError as e:
        # if the password is wrong, continue the loop
        continue