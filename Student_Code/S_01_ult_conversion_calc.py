# generates a statement.
def statement_generator(text, decoration):
    # make string with length of text
    ends = decoration * len(text)

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print("This program is created to show you (the user) the conversions of a unit you select.")
    print()
    print("If you are using Distance, write either mm, cm, m, km, in, ft, yd, mi.")
    print("This is for Millimeters, Centimeters, Metres and Kilometres for the Metric System.")
    print("Inches, Feet, Yards And Miles for American Imperial System.")
    print()
    print("If you are using Time, The Units are s, min, hr, day, week, month and year.")
    print()
    print("If you are using weight, The Units are mg, g, kg, oz, lb and ton")
    print()
    print("Complete as many calculations as necessary.")
    print()
    return ""


# converts distance from one unit to another
def convert_distance(amount, from_unit, to_unit):
    conversion_factors = {
        'mm': 0.1,
        'cm': 1,
        'm': 100,
        'km': 100000,
        'in': 2.54,
        'ft': 30.48,
        'yd': 91.44,
        'mi': 160934.4,
    }
    return amount * conversion_factors[from_unit] / conversion_factors[to_unit]


# converts time from one unit to another.
def convert_time(amount, from_unit, to_unit):
    conversion_factors = {
        's': 1,
        'min': 60,
        'hr': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2628000,
        'year': 31536000,
    }
    return amount * conversion_factors[from_unit] / conversion_factors[to_unit]


# converts weight to another unit.
def convert_weight(amount, from_unit, to_unit):
    conversion_factors = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lb': 453.592,
        'ton': 907185,
    }
    return amount * conversion_factors[from_unit] / conversion_factors[to_unit]


# main routine goes here.

# Display instructions if the user has not opened the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
while True:
    print("Select conversion type:")
    print("1. Distance")
    print("2. Time")
    print("3. Weight")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount: "))
        from_unit = input("Enter from unit: ")
        to_unit = input("Enter to unit: ")
        result = convert_distance(amount, from_unit, to_unit)
        print(f"{amount} {from_unit} = {result} {to_unit}")
    elif choice == '2':
        amount = float(input("Enter amount: "))
        from_unit = input("Enter from unit: ")
        to_unit = input("Enter to unit: ")
        result = convert_time(amount, from_unit, to_unit)
        print(f"{amount} {from_unit} = {result} {to_unit}")
    elif choice == '3':
        amount = float(input("Enter amount: "))
        from_unit = input("Enter from unit: ")
        to_unit = input("Enter to unit: ")
        result = convert_weight(amount, from_unit, to_unit)
        print(f"{amount} {from_unit} = {result} {to_unit}")
    elif choice == '4':
        print("Exiting the calculator. Thanks for utilizing me, I hope you succeed.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
