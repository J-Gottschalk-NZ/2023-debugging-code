"""
    Problem:
    The following function number_of_dogs(pets) takes a list of
    strings pets, and returns the number of times the string dog
    appears in the list. It is not case-sensitive, Dog,
    DOG and others should also be accepted.
"""


def number_of_dogs(pets):
    total = 0
    for i in range(len(pets)):
        if pets[i].lower() = "dog":
            total += i
    return total


# testing is below - code to debug is above!
to_test = [
    (["Dog", "dog", "dog", "Dog", "dog", "Dog", "Dog", "Dog", "dog", "dog"], 10),
    (["kitten", "Budgie", "rabbit", "Rainbow Lorikeet"], 0),
    (["dog", "cat", "parrot"], 1),
    (["Chinchilla", "Cat", "Dog", "Puppy", "Cat", "Cat", "Dog", "Goldfish"], 2)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = number_of_dogs(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
