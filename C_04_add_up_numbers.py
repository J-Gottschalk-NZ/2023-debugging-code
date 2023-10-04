"""
    Problem:
    The following function add_up(numbers) takes a list of numbers and adds them up.

    The function is supposed to output the sum of all the numbers,
    but there's a problem: it only outputs the first number, rather than giving the total.
"""


# Find the smallest numbers
def add_up(numbers):
    total = 0
    for number in numbers:
        total += number
        return total


# testing is below - code to debug is above!

to_test = [
    ([9, 32], 41),
    ([1, 2, 3, 4, 5], 15),
    ([65, 22, 3, 100], 190),
    ([27], 27),
    ([], 0)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = add_up(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
