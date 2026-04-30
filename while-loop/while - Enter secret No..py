"""
program to take a word from user,
until user enters correct word just like password
"""


secret = "saad"

word = input("Enter secret word:    ")
while True:
    if word==secret:
        print("You entered correct word!")
        break
    
    else:
        word = input("Enter secret word:    ")
