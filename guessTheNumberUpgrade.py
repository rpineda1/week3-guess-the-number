'Ricardo Pineda'
import random
import guessTheNumberUpgrade
# -------------------------------------------------------------------
# this is the generateNumber function
# it has one parameter:
#   'topLimit' which is the top limit for the random number generator
# the function returns the random number generated to its caller
def generateNumber( topLimit ):
    secretNumber = random.randint(1, topLimit)
    
    
    
    # TO DO: ####################################################
    # Write code in this function that calculates and           #
    # returns a random number between 1 and the user's topLimit #
    #############################################################
    
# end of generateNumber function -------------------------------------


# -------------------------------------------------------------------
# this is the askUserToGuess function
# it has two parameters:
#   the 'times' parameter is the number of guesses allowed
#   the 'secretNumber' parameter is the secret, random number
# the function returns one of two values:
#   return True if the user guessed the answer correctly
#   return False if the user did not guess the answer correctly

def askUserToGuess( times, secretNumber ):
    
    # this loop cycles through all the user guesses 
    for guessesTaken in range(1, times+1):
        print('Guess #' + str(guessesTaken) + ': ')
        guess = int(input())
        global guess
        if evaluateAnswer( guess, secretNumber ) == True:
            return True
    return False
# end of askUserToGuess function ----------------------------------


# -------------------------------------------------------------------
# this is the evaluateAnswer function
# it has two parameters:
#   the 'userGuess' parameter is the answer entered by the user
#   the 'userSecretNumber' parameter is the randomly generated number
def evaluateAnswer( userGuess, userSecretNumber ):
    if guess < secretNumber:
        print('your guess is too low try again!')
        return False
    elif guess > secretNumber:
        print('your guess is too high try again!')
        return False
    elif guess == secretNumber:
        return True
    
    # TO DO: ####################################################
    # Write code in this function that compares userGuess and   #
    # userSecretNumber. The code should:                        #
    # 1. If the user guess is smaller than the secret number,   #
    #    tell the user their guess is too low, and return False #
    # 2. If the user guess is greater than the secret number,   #
    #    tell the user their guess is too high, and return False#
    # 3. If the user guess and secret number are the same,      #
    #    return True, no message prints to the screen           #
    #############################################################

# end of evaluateAnswer function -------------------------------------


# -------------------------------------------------------------------
# this is the playGame function
# it has one parameter:
#   'showAnswer' is a Boolean value, if that Boolean value is:
#       True, we'll show the right answer on the screen
#       False, we won't show the right answer on the screen
def playGame( showAnswer ):
    theNumber == secretNumber


    # TO DO: ####################################################
    # Write code in this function that                          #
    # 1. Greets the user                                        #
    # 2. Asks the user to choose the upper limit of the random  #
    #    number generator. Store the user's response in a       #
    #    variable you define                                    #
    # 3. Asks the user to choose a total number of guesses.     #
    #    Store the user's response in a local                   #
    #    variable called 'totalGuesses'                         #
    # 4. Generates a random number using the generateNumber     #
    #    function. Ensure the random number is between 1 and    #
    #    the user's choice for the upper limit. Store this      #
    #    number in the local variable 'theNumber'               #
    # 5. Tell the user to guess a number between 1 and the      #
    #    upper limits, and tell the user how many guesses they  #
    #    have in total                                          #
    #############################################################


    
# start of game
print("Hello, let's play a game! Guess the number that I am thinking of.")
print("to start of what's the largest number you want me to guess?")
topLimit = int(input())

print('How many times would like to guess?')
totalGuesses = int(input())
            
print("okay... hmm I'm thinking of a number betweeen 1 and " + str(topLimit) + ".") 
print("you have " + str(totalGuesses) + " tries to guess it")
secretNumber = random.randint(1, topLimit)
askUserToGuess(totalGuesses, secretNumber )
theNumber = secretNumber
playGame(secretNumber)
   
# you don't need to change anything below this comment ##############
    # ///////////////////////////////////////////////////////////////////
    # this if statement allows us to show the hidden number to the user
if( showAnswer == True ):
    print('--shhh, the real number is ' + str(theNumber) + '.')
    
    #this gives a sucess/fail message if the user guessed correctly in the allotted attempts
if askUserToGuess(totalGuesses,theNumber) == True:
    print('Good job! You guessed my number!')
else:
    print('Nope. The number I was thinking of was ' + str(theNumber))
# end of playGame function -----------------------------------------
