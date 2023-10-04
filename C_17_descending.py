"""
    Problem:
    The function is_descending(items) takes a list of numbers,
    items, and returns True if each item is in descending order.

    Ascending order means each item is greater than or equal to the next item.
"""


def is_descending(items):
    result = True
    for i in range(1, len(items)):
        if i - 1 < i:
            result = False
    return result


# testing is below - code to debug is above!
to_test = [
    ([4, 3, 2, 1], True),
    ([1, 2, 3, 4], False),
    ([4, 4, 2, 2], True),
    ([4, 3], True)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = is_descending(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
