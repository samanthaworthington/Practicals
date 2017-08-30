

NUMBERS_VALUE = 5


def main():

    numbers = []

    for value in range(1, NUMBERS_VALUE + 1):
        number = int(input("Number: ".format(value)))
        numbers.append(number)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/NUMBERS_VALUE))

main()