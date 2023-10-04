"""
    Problem:
    The following function is_favourite_number(number)
    takes a number as an argument and should return True
    if it is the number 15 or 22 (someone's favourite numbers),
    otherwise it should return False.
"""


def is_favourite_number(number):
    if number == 15 or 22:
        is_favourite = True
    else:
        is_favourite = False
    return is_favourite


# testing is below - code to debug is above!
to_test = [
    (10, False),
    (19, False),
    (24, False),
    (15, True),
    (22, True)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = is_favourite_number(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
