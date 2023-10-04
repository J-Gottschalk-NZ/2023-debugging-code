"""
    Problem:

    The function below takes a string as an argument and should return the Boolean value of True
    if the string is longer than 8 characters, otherwise it should return False.
"""


# Calculate string length
def is_string_too_long(string):
    if len(string) > 8:
        is_too_long = "True"
    else:
        is_too_long = "False"
    return is_too_long


# testing is below - code to debug is above!

to_test = [("Short", False),
           ("Alliance", False),
            ("Battery", False),
            ("Crocodile", False),
            ("This string is too long", False)
           ]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = is_string_too_long(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
