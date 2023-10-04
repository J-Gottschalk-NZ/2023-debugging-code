"""
    Problem:
    The following function nth_to_last(items, n)
    takes a list (items) and a number (n), and should
    return the item nth from last in the list. In other words;
    n = 1 should return the last item, n = 2 should
    return the second to last, and so on.

    n will always be an integer between 1 and the length of the list (inclusive).
"""


def nth_to_last(items, n):
    index = items - n
    return items[index]


# testing is below - code to debug is above!
to_test = [
    ([1, 2, 3], 3, 1),
    ([1, 2, 3], 1, 3),
    (['a', 'e', 'i', 'o', 'u'], 4, 'e')
]

for item in to_test:
    # retrieve test case and expected value
    param_1 = item[0]
    param_2 = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = nth_to_last(param_1, param_2)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Expected: {expected}, received: {actual} ❌❌❌")
