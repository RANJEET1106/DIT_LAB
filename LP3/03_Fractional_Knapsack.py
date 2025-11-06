def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = []
    # Create list of (value, weight, ratio)
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((values[i], weights[i], ratio))

    # Sort by ratio descending
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    for value, weight, ratio in items:
        # If item fits fully
        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            # Take fraction
            total_value += ratio * capacity
            break
    return total_value

values  = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")

