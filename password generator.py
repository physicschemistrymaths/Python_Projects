#password generator

import random

print("Your Password:")

chars='abcdefghijklmopqrstuvwxyz123456789!@#$%^&*()?'

password=''

for x in range(10):
    password += random.choice(chars)

print(password)

#predicting euro winner

import random

def euro_winner():
    teams=["England","Netherlands","Spain","Germany",
           "Switzerland","Turkiye","France","Portugal"]

    winner=random.choice(teams)

    return winner

winner=euro_winner()
print("Euro 2024 winner is",winner)
