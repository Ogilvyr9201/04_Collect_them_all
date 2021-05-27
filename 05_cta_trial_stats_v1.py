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

trial_summary = []

trials_played = 0
purchased_ave = 0
price_ave = 0

for item in range(0, 5):
    result = int(input("choose number of items purchased: "))

    outcome = "Round {}: {}".format(item, result)
    
    trial_price = result * 3

    # Adds Game result to a list for history
    trial_summary.append("Trial #{}: {} Items purchased: ${} spent".format(trials_played + 1, result, trial_price))

    # Add to the total to be divided to make average
    purchased_ave += result
    trials_played += 1

# Calculate averages
final_ave = purchased_ave / 5
fin_price_ave = final_ave * 3

# Displays game stats with % values to the nearest whole number
print()
print("**** Trial Statistics ****")
print("Average Number of items Purchased: {}".format(final_ave))
print("Average price paid each trial: $%3.2f"%(fin_price_ave))
print()

# Asks user if they want to see there history
show_history = yes_no("would you like to see game history? ")

# displays history if user says yes
if show_history == "yes":
    print()
    print("**** Game History ****")
    for trial in trial_summary:
        print(trial)

    print()
    print("Thanks for playing")

# Doesnt display history if user says no
elif show_history == "no":
    print()
    print("Thanks for Playing")
