

COLOUR_NAMES = {"Black": "#000000", "Coral": "#ff7f50", "Brown": "#a52a2a",
                "Firebrick": "#b22222", "Goldenrod": "#daa520", "Khaki": "#f0e68c",
                "Lavender": "#e6e6fa", "Light": "#eedd82", "Maroon": "#b03060", "Medium": "#66cdaa"}

colour = input("Enter a colour name: ")

while colour != "":
    if colour.title() in COLOUR_NAMES:
        print(colour.title(), "has the hexadecimal colour code of ", COLOUR_NAMES[colour.title()])
    else:
        print("Invalid colour name")
    colour = input("Enter a colour name: ")
