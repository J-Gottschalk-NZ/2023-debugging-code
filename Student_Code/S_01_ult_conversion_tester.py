"""
    Problem:

    Create a function to convert between units of distance, time and mass.
    In this component, we are assuming that all the units have been changed
    to a valid abbreviation.  Our function should output an error (rather than crashing)
    if users choose units from different domains (eg: convert 20 mm to min).
"""


# Write your converter function below.
# You can create additional functions and call them if necessary.
def converter(amount, from_unit, to_unit):
    pass


# testing is below - code to debug is above!
to_test = [
    (3, "cm", "mm", 30),
    (3, "mm", "cm", 0.3),
    (40, "cm", "m", 0.4),
    (2, "m", "cm", 200),
    (3, "m", "mm", 3000),
    (30, "mm", "m", 0.03),
    (3, "cm", "min", "Invalid, please try again"),

           ]

for item in to_test:
    # retrieve test case and expected value
    given_amount = item[0]
    go_from = item[1]
    go_to = item[2]
    expected = item[3]

    actual = converter(given_amount, go_from, go_to)

    question = f"{given_amount} {go_to} to {go_to}"

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {question}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {question}, expected: {expected}, received: {actual} ❌❌❌")
