# import the random module
import random

# create the class Dice
class Dice:
    # create the constructor (__init__) method
    # it takes as input the number sides and if none is specified use 6
    def __init__(self, side=6):
    # it sets the dice object's number of sides (instance variable)
        self.side = side
    # it sets the list that tracks the rolls to the empty list (instance variable)
        self.rolls_list = []


    # create the __str__ method
    def __str__(self):
    # it returns "Last roll: value" where value is the last value in the list that tracks the rolls
        return "Last roll: " + str(self.rolls_list[-1])


    # create the roll method
    def roll(self):
    # it randomly picks a value from 1 to the number of sides this dice object has
        randomint = random.randint(1, self.side)
    # it adds that value to the end of the list that tracks all the rolls
        self.rolls_list.append(randomint)
    # it returns the value
        return randomint


    # BONUS
    # create the print_count_for_num method
    # it will count how many times the passed number has been rolled and print 
    # number was rolled x times - where number is the number and x is the count


# main function
def main():
    
    # Create an instance
    three_sided = Dice(3)
    print("Three sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(three_sided.roll())

    # Print last roll
    print(three_sided)

    # Create an instance
    six_sided = Dice()
    print("\nSix sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(six_sided.roll())

    # Print last roll
    print(six_sided)

    # BONUS quiz
    # Print accumulation
    #six_sided.print_count_for_num(3)

if __name__ == "__main__":
    main()
    