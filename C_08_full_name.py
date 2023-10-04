"""
    Problem:
    The following function full_name(first_name, last_name)
    takes a person's first and last name and should return
    the full name of that person.
"""


def full_name(first_name, last_name):
    print(first_name + " " + last_name)


# testing is below - code to debug is above!
to_test = [
    ("Kate", "Sheppard", "Kate Sheppard"),
    ("Malcolm", "X", "Malcolm X"),
    ("Alex", "Fraser", "Alex Fraser"),
    ("Julie", "Webb", "Julie Webb")
]

for item in to_test:
    # retrieve test case and expected value
    param_1 = item[0]
    param_2 = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = full_name(param_1, param_2)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Expected: {expected}, received: {actual} ❌❌❌")
