"""
    Problem:
    The following function is_price_in_budget(price) that
    takes the price of a mobile phone as an argument and
    should return True if the price is between $100 and $500
    (inclusive), otherwise it should return False.
"""


def is_price_in_budget(price):
    if price > 100 or price < 500:
        is_in_budget = True
    else:
        is_in_budget = False
    return is_in_budget


# testing is below - code to debug is above!
to_test = [
    (99, False),
    (100, True),
    (300, True),
    (499, True),
    (500, True),
    (501, False)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = is_price_in_budget(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
