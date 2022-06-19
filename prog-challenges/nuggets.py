"""Determine if nuggets can be ordered in quantity exactly.

Given boxes of 6, 9 and 20, can you order exactly n nuggets.
"""


past_nuggets = {}
past_nuggets2 = {}

def is_boxable(nuggets):
    """Ruturn if possible to order number of nuggets exactly."""
    if nuggets in past_nuggets:
        return past_nuggets[nuggets]

    past_nuggets[nuggets] = False
    max_boxes = nuggets / 6 + 1
    for s in range(max_boxes):
        for n in range(max_boxes):
            for t in range(max_boxes):
                if (s*6 + n*9 + t*20) == nuggets:
                    past_nuggets[nuggets] = True
                    return True

    return False

# print(is_boxable(9))
# print(is_boxable(18))
# print(is_boxable(12))
# print(is_boxable(6))
# print(is_boxable(10))
# print(is_boxable(30))
# print(is_boxable(13))
# print(is_boxable(176))
# print(is_boxable(18))
# print(past_nuggets)


def is_boxable2(nuggets):
    print('{} combos known'.format(len(past_nuggets2)))
    """recursive process to determine if possible."""
    if nuggets in past_nuggets2:
        return past_nuggets2[nuggets]
    if nuggets == 0:
        return True
    if nuggets < 0:
        return False
    else:
        past_nuggets2[nuggets - 6] = is_boxable2(nuggets - 6)
        past_nuggets2[nuggets - 9] = is_boxable2(nuggets - 9)
        past_nuggets2[nuggets - 20] = is_boxable2(nuggets - 20)
        return (is_boxable2(nuggets - 6) or
                is_boxable2(nuggets - 9) or
                is_boxable2(nuggets - 20))

# print(is_boxable2(4229))
# print(is_boxable2(18))
# print(is_boxable2(12))
# print(is_boxable2(18))


known_boxable = {}

def is_boxable3(nuggets):
    if nuggets in known_boxable:
        return known_boxable[nuggets]

    if nuggets < 0:
        return False
    elif nuggets == 0:
        return True
    else:
        known_boxable[nuggets - 6] = is_boxable3(nuggets - 6)
        known_boxable[nuggets - 9] = is_boxable3(nuggets - 9)
        known_boxable[nuggets - 20] = is_boxable3(nuggets - 20)
        return is_boxable3(nuggets - 6) or is_boxable3(nuggets - 9) or is_boxable3(nuggets - 20)


print(is_boxable3(8232))
print(is_boxable3(26))
print(known_boxable)
