# imports 
import os
import random
import string
import numpy as np

# create a function to list the files in the current working directory
def list_files(path="."):
    return (os.listdir(path))


# a simple dice game that doesn't return anything
def roll_dice():
    roll = random.choices(range(1,7), k=2)
    print(f'You rolled a {roll[0]} and {roll[1]}.')
    if roll[0] == roll[1]:
        print ("Congrats, you win because you rolled the same value!")
    else:
        print ("Try again.  The goal is to have the values from each dice match.")
    
    pass



# a simple guess my number game
def guessing_game():
    np.random.seed(765)
    guess = int( input("Guess a number from 1 to 10: ") )
    actual = int(random.choice(range(1,11)))
    if guess == actual:
        print("Congrats, you are correct!")
    else:
        print("Sorry, try again.  The number was {}".format(actual))
    
    pass


# a simple random email generator
def email_generator(n=50):
    # setup
    domains = ["gmail.com","hotmail.com", "aol.com", "yahoo.com"]
    letters = string.ascii_lowercase
    # the list to house the emails
    emails = []
    # build the emails
    np.random.seed(765)
    for _ in range(n):
        chars = np.random.choice(list(letters), np.random.randint(1,10))
        chars = list(chars)
        chars = ''.join(chars)
        domain = np.random.choice(domains, 1)[0]
        email = chars + '@' + domain
        emails.append(email)
    # return the list
    return emails
