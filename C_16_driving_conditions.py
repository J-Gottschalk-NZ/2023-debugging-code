"""
    Problem:
    The following function check_danger_level(is_dark, is_wet) returns
    the current level of danger for the driver. Where is_dark,
    is_wet are both booleans (True/False)

    If it's both dark and wet return The driving conditions are currently VERY dangerous!!
    If it's either dark or wet return The driving conditions are currently dangerous!

    Otherwise, return It's a nice day for a drive.
"""


def check_danger_level(is_dark, is_wet):
    if is_dark is True and is_wet is True:
        return 'The driving conditions are currently VERY dangerous!!'
    elif is_dark is True or is_wet is True:
        return 'The driving conditions are currently dangerous!'
    else:
        return 'It's a nice day for a drive.'



# testing is below - code to debug is above!
to_test = [
    (True, True, "The driving conditions are currently VERY dangerous!!"),
    (True, False, "The driving conditions are currently dangerous!"),
    (False, True, "The driving conditions are currently dangerous!"),
    (False, False, "It's a nice day for a drive.")
]

for item in to_test:
    # retrieve test case and expected value
    param_1 = item[0]
    param_2 = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = check_danger_level(param_1, param_2)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Expected: {expected}, received: {actual} ❌❌❌")
