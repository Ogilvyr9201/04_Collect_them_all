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

# Asks user for the word
# Repeated for testing purposes
word = word_checker("What is the Word? ", "<error> Inptut a word more then 1 character long")
print(word)
print()

# Turns word into a list of characters
word_list = list(word)
print(word_list)