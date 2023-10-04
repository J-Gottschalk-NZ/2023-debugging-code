"""
    Problem:
    The following function dozens_of_eggs(num_egs)
    takes the number of eggs that you have and returns
    how many whole dozens are in that many eggs.
"""


def dozens_of_eggs(num_eggs):
    dozens = num_eggs / 12
    return f"There are {dozens} dozen eggs!"


# testing is below - code to debug is above!
to_test = [
    (11, "There are 0 dozen eggs!"),
    (89, "There are 7 dozen eggs!"),
    (12, "There are 1 dozen eggs!"),
    (0, "There are 0 dozen eggs!"),
    (17, "There are 1 dozen eggs!")
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = dozens_of_eggs(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
