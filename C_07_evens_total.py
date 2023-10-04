"""
    Problem:
    The following function total_of_even_numbers takes a
    list of numbers and returns the sum of the even numbers in the list.
"""


def total_of_even_numbers(numbers):
    even_total = 0
    for number in numbers:
        if number % 2 == 0:
            even_total += number
            return even_total


# testing is below - code to debug is above!
to_test = [
    ([1, 2, 3, 4, 5, 6], 12),
    ([2, 4, 6, 8, 10], 30),
    ([-7, 4, 42, -12, 0, 0, 18], 52),
    ([0], 0)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = total_of_even_numbers(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
