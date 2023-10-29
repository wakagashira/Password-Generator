#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
varTotalChar = nr_letters + nr_numbers + nr_symbols
varFullPW = ""
for Loop1 in range(varTotalChar):
  varNextLetter = random.choice(letters)
  varNextNumber = random.choice(numbers)
  varNextSymbols = random.choice(symbols)
  VarChoices = []
  if nr_letters > 0:
    VarChoices.append(varNextLetter)
  if nr_numbers > 0:
    VarChoices.append(varNextNumber)
  if nr_symbols > 0:
    VarChoices.append(varNextSymbols)
  VarPWChar = random.choice(VarChoices)
  if VarPWChar in letters:
    nr_letters -= 1
  if VarPWChar in numbers:
    nr_numbers -= 1
  if VarPWChar in symbols:
    nr_symbols -= 1
  varFullPW += VarPWChar
print(f"Your Password is: {varFullPW}")
