#  Each type of cake has a weight and a value, stored in a tuple with two indices:
#
#     An integer representing the weight of the cake in kilograms
#     An integer representing the monetary value of the cake in British shillings
#
# For example:
# Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)
# Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)

# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns
# the maximum monetary value the duffel bag can hold.
#
# For example:
# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
# max_duffel_bag_value(cake_tuples, capacity)


def max_duffel_bag_value(cake_tuples, capacity):
    total_capacity = 0
    total_value = 0
    while total_capacity < capacity:
        max_capacity = 0
        max_value = 0
        rest_of_capacity = capacity - total_capacity
        for cake_size, cake_val in cake_tuples:
            cakes_in_bag = rest_of_capacity // cake_size
            if cakes_in_bag == 0:
                continue
            bag_val = cakes_in_bag * cake_val
            if bag_val > max_value:
                max_capacity = cakes_in_bag * cake_size
                max_value = bag_val
        if max_value == 0:
            break
        total_capacity += max_capacity
        total_value += max_value

    return total_value
