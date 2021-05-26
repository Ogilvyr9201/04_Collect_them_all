# Functions go here
def num_check(question, error, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = float(input(question))

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


# Main Routine
# Looped fpr testing
while 1 == 1:
    # Ask user for the item
    item_error = "<error> enter the price eg: 4 or 4.5"
    item_cost = num_check("What is the cost of the Item? ", item_error, 0)
    # Output item back (credit to https://www.python-course.eu/python3_formatted_output.php 
    # for info on how to out put variable as a float)
    print("Item Cost: $%3.2f"%(item_cost))
    print()
    break