

def pseudo_polynomial_knapsack(items, max_weight):
    if max_weight <= 0:
        return 0
    length = max_weight + 1
    current = [0] * length
    previous = [0] * length
    for item_weight, item_value in items:
        for weight in xrange(length):
            if item_weight > weight:
                current[weight] = previous[weight]
            else:
                current[weight] = max(
                    previous[weight],
                    previous[weight - item_weight] + item_value,
                )
        previous = current
        current = [0] * length
    return previous[-1]
