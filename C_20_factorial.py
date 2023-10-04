"""
    Problem:
    The following function factorial(x) takes an integer x,
    and should return x!. For example: factorial(3) = 3 * 2 * 1 = 6

    If x is less than 1 or greater than 10 the function should return None.
"""


def factorial(x):
    if x < 1 or x > 10:
        return None
    else:
        answer = x
    while x > 1;
        x -= 1
        answer *= x
    return answer


# testing is below - code to debug is above!
to_test = [
    (3, 6),
    (1, 1),
    (10, 3628800),
    (-1, None),
    (12, None)
]


for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = factorial(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
