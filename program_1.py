
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    rand1 = random.randint(float(1, 6))
    rand2 = random.randint(float(1, 6))

    # Sum 2 numbers
    randsum = rand1 + rand2

    # return sum to calling function
    return randsum
    for randDice() in range(100):
        final_result = randDice / 100
        print(final_result)

    #########
    # Then write a mainline that calls the "randDice" function 100 times in a for loop.
    # The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
