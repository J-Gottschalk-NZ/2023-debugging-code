"""
    Problem:
    The following function discounted_cost(price, discount_percent) takes two arguments:

    price: The original price of the item
    discount_percent: The discount that should be applied to the item,
    e.g. 20 for a 20% discount.

    It should return the discounted cost of the item.
"""


def discounted_cost(price, discount_percent):
    discount = price * discount_percent
    cost = price - discount
    return f"${cost:.2f}"


# testing is below - code to debug is above!
to_test = [
    (99, 10, "$18.90"),
    (50, 25, "$37.50"),
    (100, 15, "$85.00"),
    (26, 0, "$26.00")

]

for item in to_test:
    # retrieve test case and expected value
    param_1 = item[0]
    param_2 = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = discounted_cost(param_1, param_2)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Expected: {expected}, received: {actual} ❌❌❌")
