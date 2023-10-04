"""
    Problem:
    The following function find_highest_number(numbers)
    takes a list of numbers as an argument, and should
    return the highest/maximum number in the list. .
"""


def find_highest_number(numbers):
    highest_number = 0
    for num in numbers:
        if num > highest_number:
            highest_number = num
    return highest_number


# testing is below - code to debug is above!
to_test = [
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 5),
    ([15, 50, 10, 45], 50),
    ([0, 0, 0, -1], 0),
    ([-7, -15, -29, -3], -3)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = find_highest_number(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
