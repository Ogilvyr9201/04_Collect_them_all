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


# Checks for yes or no responses Imported From LU
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Instructions will be displayed when this function is called
def instructions():
    print(
        "Welcome to Collect them all, this program\n"
        "allows you to choose an item that will be\n"
        "purchased along with a token. These token\n"
        "will be able to spell out the item you chose\n"
        "and when you can spell it out you get a reward.\n"
        "\n"
        "This Program calculates the average amount\n"
        "of that item needed to be purchased before\n"
        "you spell out the word as well as how much\n"
        "it costs.\n"
        "\n"
        "You can also see how much for each trial after\n"
        "but I recommend you only do this if you have\n"
        "30 or less trials. "
    )
    return""

# Main Routine goes here
# Errors (Used to make lines shorter)
word_error = "<error> Inptut a word more then 1 character long"
trial_error = "<error> Please enter an interger above 0"
item_cost_error = "<error> enter the price eg: 4 or 4.5"

# Title
statement_generator("Collect them all", "!", "=")

used_before = yes_no("Have you used the program before? ")
if used_before == "yes":
    print()
    instructions()
    print()


play_again = "true"
while play_again == "true":

    # resets everything for program to use again
    trial_summary = []
    trials_played = 0
    purchased_ave = 0
    price_ave = 0
    num_items = 0
    trial_price = 0

    # Asks User for the word
    word = word_checker("What is the Word? ", word_error)

    # Turns word into a list of characters
    word_list = list(word)
    statement_generator("TOKENS", "*", "")
    print(word_list)
    print()

    # Comparrison list (removes item when it is found)
    comparrison_list = word_list

    # Asks user for the cost of the item
    item_cost = num_check("What is the cost of the Item? ", item_cost_error, float, 0)
    print()

    # Asks user for the amount of trials
    num_trials = num_check("What is the number of trials? ", trial_error, int, 0)
    print()
    # Saves trial number
    trial_save = num_trials
    # repeats program till it is finished
    while num_trials > 0:

        # Generates tokens to remove from list
        token_choice = random.choice(word_list)

        # compares if the token is in the comparrison list if it is it removes it
        if token_choice in comparrison_list:
            # adds correct letter into the list
            comparrison_list.remove(token_choice)    

        # program repeats untill the list is empty
        if len(comparrison_list) > 0:
            # adds number of items purchased
            num_items += 1
            # Sets word list to keep all tokens or else program will run best case 100% 
            word_list = list(word)
        else:
            # gets price and total amount of items purchased
            num_items += 1
            trial_price = num_items * item_cost

            # Add to the total to be divided to make average
            purchased_ave += num_items
            trials_played += 1
            
            # decreases number of trials left to do
            num_trials -= 1

            # Appends result to a list for stats
            trial_summary.append("Trial #{}: {} Items purchased: ${} spent".format(trials_played, num_items, trial_price))

            # resets everything for program to use again
            num_items = 0
            trial_price = 0
            comparrison_list = word_list

    # Calculate averages
    final_ave = purchased_ave / trial_save
    fin_price_ave = final_ave * item_cost 

    # Displays trial stats, Average amount of items purchased and cost
    statement_generator("Trial Statistics", "!", "=")
    print()
    print("Average Number of items Purchased: {}".format(final_ave))
    print("Average price paid each trial: $%3.2f"%(fin_price_ave))
    print()

    # Asks user if they want to see there history
    show_history = yes_no("Would you like to see trial history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Trial History", "$", "=")
        print()
        for trial in trial_summary:
            print(trial)

        print()
        play_again = yes_no("Would you like to use again? ")
        if play_again == "yes":
            play_again = "true"
        else:
            play_again = "false"

    # Doesnt display history if user says no
    elif show_history == "no":
        print()
        # Asks user if they want to use again
        play_again = yes_no("Would you like to use again? ")
        if play_again == "yes":
            play_again = "true"
        else:
            play_again = "false"
