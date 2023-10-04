"""
    Problem:
    The following function evens_out(numbers) is supposed to
    take a list of numbers and return a new list containing
    only the odd numbers from the original list.
"""


def evens_out(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


# testing is below - code to debug is above!

to_test = [
    ([1, 2, 3, 4, 5, 6], [1, 3, 5]),
    ([2, 43, 996, 89, 425, 32, 78], [43, 89, 425]),
    ([2, 4, 6, 8, 10], []),
    ([3, 1, 5, 9, 7, 11], [3, 1, 5, 9, 7, 11]),
    ([42, 9, 17, 84], [9, 17])
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = evens_out(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
