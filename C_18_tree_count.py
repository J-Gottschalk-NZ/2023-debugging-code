"""
    Problem:
    Write a function is_forest(items) that takes a Python list of strings,
    items, and returns a boolean (True/False) telling us if the list
    contents form a forest.

    In this scenario any group of items with more than one tree is a
    forest. A tree can be lowercase or start with a capital letter.
"""


def is_forest(items):
    tree_count = items.count("tree")
    tree_count = items.count("Tree")
    return tree_count > 1



# testing is below - code to debug is above!
to_test = [
    (["Bush", "River", "Tree", "Tree", "Shrub"], True),
    (["Tree", "tree"], True),
    (["bush", "river", "tree", "shrub"], False),
    (["Bush", "River", "Tree", "Shrub"], False),
    (["bush", "river", "tree", "tree", "shrub", "tree"], True),
    (["bush", "river", "tree", "tree", "shrub"], True)
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = is_forest(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
