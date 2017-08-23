

def main():

    name = get_name()

    print(name[0:len(name):2])


def get_name():
    name = str(input("What is your name? "))
    while len(name) <= 0:
        print("No name entered")
        name = str(input("What is your name? "))
    return name


main()






