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

# resets everything for program to use again
trial_summary = []

trials_played = 0
purchased_ave = 0
price_ave = 0

play_again = "true"
while play_again == "true":

    # resets everything for program to use again
    num_items = 0
    trial_price = 0

    # Asks User for the word
    word = word_checker("What is the Word? ", word_error)
    print(word)
    print()

    # Turns word into a list of characters
    word_list = list(word)
    print("*** TOKENS ***")
    print(word_list)
    print()

    # Comparrison list (removes item when it is found)
    comparrison_list = word_list

    # Asks user for the cost of the item
    item_cost = num_check("What is the cost of the Item? ", item_cost_error, float, 0)
    print()

    # Asks user for the amount of trials
    num_trials = num_check("What is the numebr of trials? ", trial_error, int, 0)
    print()

    # repeats program till it is finished
    while num_trials > 0:
        # Generates tokens to remove from list
        token_choice = random.choice(word_list)
        print(token_choice)

        # compares if the token is in the comparrison list if it is it removes it
        if token_choice in comparrison_list:
            # adds correct letter into the list
            comparrison_list.remove(token_choice)    

        # program repeats untill the list is empty
        if len(comparrison_list) > 0:
            # gets price and total amount of items purchased
            num_items += 1
            trial_price = num_items * item_cost

            # Appends result to a list for stats
            trial_summary.append("Trial #{}: {} Items purchased: ${} spent".format(trials_played + 1, num_items, trial_price))
            
            # Sets word list to keep all tokens or else program will run best case 100% 
            word_list = list(word)

            # Add to the total to be divided to make average
            purchased_ave += num_items
            trials_played += 1
        else:
            # adds number of items purchased and price
            num_items += 1
