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

# Comparrison list (removes item when it is found)
comparrison_list = word_list

#  testing loop generate 20 tokens
play_again = False
while not play_again:
    token_choice = random.choice(word_list)
    print(token_choice)

    # comparrisons
    if token_choice in comparrison_list:
        # adds correct letter into the list
        comparrison_list.remove(token_choice)    

    # to repeat the program
    if len(comparrison_list) > 0:
        play_again = False
        # Sets word list to keep all tokens or else program will run best case 100% 
        word_list = list(word)
    else:
        play_again = True

print("you win")
