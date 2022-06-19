#
# You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.
# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
#
# Each type of cake has a weight and a value, stored in a tuple with two indices:
#
# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British pounds
# For example:
#
# You brought a duffel bag that can hold limited weight, and you want to make
# off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type
# tuples and a weight capacity, and returns the maximum monetary value the
# duffel bag can hold.
#
# For example:
#
# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20
#
# max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20


def value_per_pound(cake_tuple):
    """Value per pound of cake."""
    cake_weight, cake_value = cake_tuple
    return float(cake_value)/float(cake_weight)


def max_duffel_bag_value(cake_tuples, capacity):
    """Return the max haul given the weights/value and capacity."""
    cake_tuples = sorted(cake_tuples, key=value_per_pound, reverse=True)
    value_of_haul = 0
    for cake_tuple in cake_tuples:
        cake_weight, cake_value = cake_tuple
        cakes_taken, capacity = divmod(capacity, cake_weight)
        value_of_haul += cakes_taken * cake_value
    return value_of_haul


print(max_duffel_bag_value(cake_tuples, capacity))
