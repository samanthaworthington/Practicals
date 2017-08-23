"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    if 0 <= score < 50:
        print("Bad")
    elif 50 <= score < 90 :
        print("Pass")
    elif 90 <= score <= 100:
        print("Excellent")
    else:
        print("Invalid Score")

main()

