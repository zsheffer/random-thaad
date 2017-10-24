import random

allowedInputs   = ["1","2"]   # we are just going to deal with string
mappedInputs    = ["Thad","Thaad"]   # we are just going to deal with string

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
