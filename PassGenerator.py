import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbole: list[str] = ['!', '#', '@', '$', '%', '&', '+', '-']

nr_letters = int(input("how many letters you want? "))
nr_numbers = int(input("how many numbers you want? "))
nr_symbole = int(input("how many symbole you want? "))

password = ""

for i in range(0, nr_letters):
    x = random.choice(letters)
    password += x
    # password_list.append(x)
for i in range(0, nr_numbers):
    x = random.choice(numbers)
    password += str(x)
    # password_list.append(str(x))
for i in range(0, nr_symbole):
    x = random.choice(symbole)
    password += x
    # password_list.append(x)
print(f"EASY WAY: {password}")

# HARD WAY
Password = ""
password_list = []
for char in password:
    password_list.append(char)

random.shuffle(password_list)
for char in password_list:
    Password += char

print(f"HARD WAY: {Password}")




