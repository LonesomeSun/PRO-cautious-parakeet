import hang2
# / / / Creating the choose players and what it does \ \ \
def p_number():  # Define the function for choosing 1 or 2 players
    player = input("Amount of players (1 or 2) ")  # Asks the user for what they want
    if player == "1":  # If player chosen is 1 then send to oneP function
        oneP()  # Calls on the oneP function
    elif player == "2":  # If player chosen is 1 then send to oneP function
        twoP()  # Calls on the twoP function
    else:  # This is where incorrect options go
        print("That is not an option")
        p_number()  # It is repeated to start this function again


def oneP():  # function for when 1 player is chosen
    global word  # sets it as global so it can be used more than locally
    word = random.choice(words).upper()  # chooses a random word from the word list, makes it uppercase
    while ' ' in word or '-' in word:  # repeats the loop if there is a space or dash because this is a public wordlist
        word = random.choice(words).upper()
    game(word)  # starts the loop for the game to actually start with the random word as the word variable
    return word


def twoP():  # function for when 2 players is chosen
    global word  # set it as global so it can be used more than locally
    word = input("Enter your secret word to be guessed. ").upper()  # lets player 2 pick a word and makes it uppercase
    if word.isalpha():  # if the word is a part of the alphabet continue

        # prints spaces so player 1 can't see the word
        print("""
























        """)
        game(word)  # starts the game with the input as the word
    else:  # stops code that isn't part of the alphabet to prevent unguessable words
        print("That is not valid!")
        twoP()


# / / / Getting the Word \ \ \
import random  # import random function of python
from wordlist import words  # in the wordlist.py file import the words list


print("Welcome to my python Hangman Game")  # prints the basic hello introduction to the game









def game(word):  # Inside of a function so that it can be restarted later on
    # / / / Some initialization \ \ \
    progress = "_" * len(word)  # creates the underscores for the word by repeating underscores by the amount of letters in the word
    guessed_letters = []  # creates a list for the letters that have been guessed
    uncovered = False  # Boolean for if the word is guessed yet
    tries = 6  # Tries that you have, traditional hangman has 6

    input("Okay lets start! Press enter")  # gets user to press enter to start so that they are ready
    print("""




    """)

    # / / / Actual game loop that continues till won or lost, put in here to restart later on \ \ \
    while tries > 0 and not uncovered:  # Checks if won or lost

        # / / / Display every turn \ \ \
        print(f"Letters Guessed:{guessed_letters}")  # letters guessed
        print(hangmanmodel(tries))  # displays the hangman model depending on how many tries left
        print(progress)  # displays the underscores indicating the progress of the user
        guess = input("Please guess a letter.").upper()  # asks the user for a letter and converts it into all uppercase

        # / / / Program checking if the letter is good \ \ \
        if len(guess) == 1:  # Check if it is a single letter
            if guess.isalpha():  # Check if it is part of the alphabet
                if guess in guessed_letters:  # Filters through checking if its already guessed
                    print("This has already been guessed")  # telling the user that it has beeen guessed already
                elif guess not in word:  # Filters through checking if its in word
                    print("Nice try but that's not in the word")  # telling the player nice try
                    tries -= 1  # reduces the value of tries by 1
                    guessed_letters.append(guess)  # adding the guessed letter to the guessed letters list to be displayed next turn

                else:  # This is the result of filtering, it should be correct
                    print("Well done, this is a letter of the word.")  # prints to the user that they have guessed it right
                    guessed_letters.append(guess)  # adding the guessed letter to the guessed letters list to be displayed next turn

                    # / / / Code Snippet from Stack Overflow because I could not implement Zarzour's code snippet \ \ \
                    word_as_list = list(progress) #  has the progress in list form
                    indices = [i for i, letter in enumerate(word) if letter == guess]  # setting a list value for indices
                    for index in indices: # a for loop for index in the value of indices
                        word_as_list[index] = guess #  Edits the underscore of value index of the word to the guess
                    progress = "".join(word_as_list) #  Joins the edited underscore list back into the progress variable
                    if "_" not in progress: #  If there is no underscores left in the word then it set boolean value of uncovered to  True
                        uncovered = True
                    # / / / End of Snippet \ \ \




            else:  # if the character is not part of the alphabet, do not accept, let while loop restart
                print("That is not part of the alphabet.")
                input("Press enter to continue")
        else:  # of the character is larger than 1 character, do not accept, let while loop restart
            print("That is not 1 character.")
            input("Press enter to continue")

        if tries == 0:  # when tries run out, show the full hangman and use the restart function with parameter lost
            print(hangmanmodel(tries))
            restart("lost")

        elif uncovered is True:  # when word is fully guessed, use the restart function with parameter as lost
            restart("won")

# / / / Making the hangman models \ \ \
def hangmanmodel(tries):  # making in a function to call it easier
    models = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   ---------------
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   --------------
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   ------------
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   ------------
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   ------------
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -----------
                   """,
                   """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -----------
                   """
    ]
    return models[tries]  # returns the correct model of value tries to display that hangman

# / / / Restart loop \ \ \
def restart(outcome):  # defining the loop to restart
    print(f"GG, you {outcome}")  # shows to user gg you won.lost depending on the game outcome
    print(f"The word was {word}")  # tells the user the word
    again = input("Would you like to restart? Yes or No ")  # asks for a restart
    if again == "Yes":  # calls the function to pick player number again
        print("""





        """)
        p_number()
    elif again == "No":  # says bye bye before exiting
        print("Bye Bye")
        exit()
    else:  # says that it is not a valid option restarting the restart function
        print("That is not a valid option")
        restart(outcome)



p_number()  # starts the pick amount of players function when the program begins
