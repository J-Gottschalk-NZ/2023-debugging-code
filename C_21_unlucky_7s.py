"""
    Problem:
    The following function sum_unlucky_7(numbers) takes a
    list of integers as an argument, and should return the
    sum of elements in the list. However, the number 7 is
    an unlucky number. All 7s should be ignored, and any non-7
    numbers immediately after a 7 should also be ignored.
"""


def sum_unlucky_7(numbers):
    total = 0
    ignore_next = False
    for num in numbers:
        if num == 7:
            ignore_next = True
        else:
            if ignore_next:
                ignore_next = False
                total += num

    return total


# testing is below - code to debug is above!
to_test = [
    ([6, 13, 1, 7, 4, 2], 22),
    ([7, 7, 7], 0),
    ([7, 12, 7, 2, 1, 3, 7, 8, 1], 5),
    ([1, 78, 2, 13, 8, 7], 102),
    ([22, 26, 11, 17, 24], 100)
    ]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = sum_unlucky_7(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
