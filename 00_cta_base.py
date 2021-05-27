# Imports
import random


# Functions go here
# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# Word checker that makes sure user inputs a word
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



# Main Routine goes here
# Errors (Used to make lines shorter)
word_error = "<error> Inptut a word more then 1 character long"
trial_error = "<error> Please enter an interger above 0"
item_cost_error = "<error> enter the price eg: 4 or 4.5"

play_again = "true"
while play_again == "true":

    # Asks User for the word
    word = word_checker("What is the Word? ", word_error)
    print(word)
    print()

    # Turns word into a list of characters
    word_list = list(word)
    print("*** TOKENS ***")
    print(word_list)
    print()

    # Asks user for the cost of the item
    item_cost = num_check("What is the cost of the Item? ", item_cost_error, float, 0)
    print()

    # Asks user for the amount of trials
    num_trials = num_check("What is the numebr of trials? ", trial_error, int, 0)
    print()
