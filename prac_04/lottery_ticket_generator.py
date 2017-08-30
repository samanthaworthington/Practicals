
import random

NUMBERS_PER_LINE = 6
SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45


def main():

    number_of_tickets = int(input("How many quick picks do you wish to generate? "))

    while number_of_tickets < 0:
        print("Please enter a valid number: ")
        number_of_tickets = int(input("How many quick picks do you wish to generate? "))

    for ticket in range(number_of_tickets):
        quick_pick = []
        for i in range(NUMBERS_PER_LINE):
            number = random.randint(SMALLEST_NUMBER,LARGEST_NUMBER)
            while number in quick_pick:
                number = random.randint(SMALLEST_NUMBER,LARGEST_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()