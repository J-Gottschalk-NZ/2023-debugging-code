keep_going = ""
while keep_going == "":
 while True:
    error = "please enter a number more than 0 "
    try:
        width = float(input("width? "))
        if width > 0:
            break

        else:
            print(error)
            print()

    except ValueError:
        print(error)

while True:
    error = "please enter a number more than 0 "
    try:
        height = float(input("height? "))
        if height > 0:
            break

        else:
            print(error)
            print()

    except ValueError:
        print(error)

area = width * height
perimeter = 2 * (width + height)
print("Perimeter: = {:.2f} units".format(perimeter))
print("Area: = {:.2f} square units".format(area))
keep_going = input("press <enter> to keep going or any key to quit")

