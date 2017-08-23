

# get x and y inputs
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y (that is greater than x): "))

MENU ="""E - show the even numbers from x to y
O - show the od numbers from x to y
S - show the sqaures from x to y
Q - quit the program"""
print(MENU)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "E":
        for i in range(x, y, 2):
            print(i, end=' ')
        print()

