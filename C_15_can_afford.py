"""
    Problem:
    The following function can_afford(balance) takes your balance in
    dollars and should return the best tablet you can afford.

    Noshiba tablets cost a minimum of $500
    ePads cost a minimum of $1000
    If users can't afford either tablet, the function should return "Nothing"
"""


def can_afford(balance):
    tablet = "Nothing"

    if balance >= 500:
        tablet = "Noshiba Sandibook"
    elif balance >= 1000:
        tablet = "ePad"

    return tablet


# testing is below - code to debug is above!
to_test = [
    (1000, "ePad"),
    (500, "Noshiba Sandibook"),
    (360, "Nothing"),
    (1840, "ePad")
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = can_afford(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
