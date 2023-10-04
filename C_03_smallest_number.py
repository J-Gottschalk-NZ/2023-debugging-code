"""
    Problem:
    The following function smallest_number(numbers)
    takes a list numbers as an argument and should return
    the smallest number in the list.
"""


# Find the smallest numbers
def smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
            return smallest


# testing is below - code to debug is above!

to_test = [([3, 5, 6, 7, 4, 2], 2),
           ([4, 5, 8, 3, 2, 1], 1),
           ([-1, 2, 3, 4, 5], -1),
           ([10, 4, 18, 5, 187], 4),
           ([-10, -20, -30, -18, -4], -30)
           ]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = smallest_number(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
