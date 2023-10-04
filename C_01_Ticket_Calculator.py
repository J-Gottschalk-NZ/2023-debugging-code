"""
    Problem:

    Free for people 5 years old and younger.
    $10 for people 12 years old and younger.
    $16 for everyone older than 12 years old.
"""


# Calculate ticket price based on age
def get_ticket_price(age):
    if age < 5:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 16
    return price


# testing is below - code to debug is above!
to_test = [(3, 0),
           (5, 0),
           (8, 10),
           (12, 10),
           (23, 16)
           ]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = get_ticket_price(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
