import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#Main Program
print("Welcome to the PyPassword Generator!")
print()
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Creates an empty list
password_list = []

for char in range(1, nr_letters + 1):
    #Adds a random letter to the list
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    #Adds a random symbol to the list
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    #Adds a random number to the list
  password_list += random.choice(numbers)
#Shuffles the characters inside the list
random.shuffle(password_list)
#Creates an empty string
password = ""
#Adds the shuffled characters to the empty string
for char in password_list:
  password += char
print(f"Your password is: {password}")