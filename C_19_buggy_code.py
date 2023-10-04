"""
    Problem:
    The following function remove_bugs(buggy_code) takes a
    list of strings as an argument, and should return a new list with all strings bug removed.
"""


def remove_bugs(buggy_code):
    for i in range(len(buggy_code)):
        if buggy_code[i] != 'bug':
            debugged_code.append(buggy_code[i])
    return buggy_code


# testing is below - code to debug is above!
to_test = [
    (['def hello_world():', 'bug', 'print("hello world")'], ['def hello_world():', 'print("hello world")']),
    (['no', 'bugs', 'here'], ['no', 'bugs', 'here']),
    ([], []),
    (['bug', 'bug'], [])
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = remove_bugs(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
