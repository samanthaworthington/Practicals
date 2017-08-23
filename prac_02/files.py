

name_file = open("name.txt", 'w')
name = str(input("Enter your name: "))
print("{}".format(name), file=name_file)
name_file.close(


name_file = open("name.txt", 'w')
name1 = str(input("Enter you name: "))
print("Your name is {}".format(name1), file=name_file)
name_file.close(


number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
print(number1 + number2)
number_file.close()


