# from random import randint

# name = raw_input("Hi, what's your name? ")
# print "%s, let's play a guessing game!" % name

# rand = randint(1, 100)
# print "random number:", rand

# guess =int(raw_input("I'm thinking of a number between 1 and 100. Guess my number: "))


# while True:
#     if guess > rand:
#         print "Your  guess is too high, try again."
#         guess = int(raw_input("Your guess? "))
#     elif guess < rand:
#         print "Your guess is too low, try again."
#         guess = int(raw_input("Your guess? "))
#     else:
#         print "Congratulations, %s, you guessed my number!" % name
#         break
       

# Greet the Player
name = raw_input("Hi, what's your name? ")
print "%s, let's play a guessing game!" % name

# Generate random number.
from random import randint
rand = randint(1, 100)
print "random number: ", rand

# User guess
try:
    guess = int(raw_input("I'm thinking of a number between 1 and 100. Guess my number: "))
except:
    print "This is not an integer."
    guess = int(raw_input("Your guess? "))

# Number of tries
tries = 0

# While loop
while True:
    if guess > 100 or guess < 1:
        print "Your guess is out of range. Please pick a number from 1 to 100."
        guess = int(raw_input("Your guess? "))
    elif guess > rand:
        print "Your guess is too high, try again."
        guess = int(raw_input("Your guess? "))
        tries += 1
    elif guess < rand:
        print "Your guess is too low, try again."
        guess = int(raw_input("Your guess? "))
        tries += 1
    else:
        tries += 1
        print "Congratulations, %s, you guessed my number in %s tries!" % (name, tries)
        play_again = raw_input("Would you like to play again? Y/N > ")
        if play_again == "Y" or play_again == "y":
            rand = randint(1, 100)
            print "random number: ", rand
            guess = int(raw_input("I'm thinking of a number between 1 and 100. Guess my number: "))
            tries = 0
        elif play_again == "N" or play_again == "n":
            print "Goodbye, %s" % name
            break
        else:
            print "That's not a valid answer. Please choose 'Y' or 'N'."
            play_again = raw_input("Would you like to play again? Y/N ")

