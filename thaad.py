import random

# TODO
# - allow scores to persist
# - set up allowed/map as dict
# - wrap properly in main functions
# - add UI with buttons to make this easier

allowedInputs   = ["1","2"]             # we are just going to deal with string
mappedInputs    = ["Thad","Thaad"]      # we will map to the pretty name after

answer          = random.choice( allowedInputs )
mappedAnswer    = mappedInputs[ allowedInputs.index(answer) ]

guess = raw_input("Enter (1) for Thad or (2) for Thaad: ")

if guess in allowedInputs:
    if answer == guess:
        print "Woohoo! " + mappedAnswer + " was the answer"
    else:
        print "Sorry! That was wrong... " + mappedAnswer + " was the answer"
else:
    # user inputted value that doesn't match, send warning
    print "That input doesn't work - try again"
