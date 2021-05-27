import random

# Functions go here
def word_checker(question, error):
    valid = False
    while not valid:

        response = input(question)

        # Checks how long word is
        if len(response) == 1:
            print(error)
            print()
            continue
        else:
            return response



# Main routine goes here

# main routine
# Ask user for the word
word = word_checker("What is the Word? ", "<error> Inptut a word more then 1 character long")
print(word)
print()

# Turns word into a list of characters
word_list = list(word)
print(word_list)

# Token list 
token_list = []
complete_list = []

#  testing loop generate 20 tokens
play_again = False
while not play_again:
    token_choice = random.choice(word_list)
    print(token_choice)

    # comparrisons
    if token_choice not in token_list:
        # adds correct letter into the list
        complete_list.append(token_choice)

    # Adds choice to a list
    token_list.append(token_choice)

    # to repeat the program
    again = input("press <enter> to play again ")
    if again == "":
        play_again = False
    else:
        play_again = True

print(token_list)
print(complete_list)
print()

a = set(word_list)
b = set(complete_list)

print(a)
print(b)
print()

if a == b:
    print("win")
else:
    print("lose")