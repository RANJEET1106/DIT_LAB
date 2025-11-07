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


n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n): 
    w = int(input(f"Enter weight for item {i+1}: "))
    weights.append(w)

for i in range(n):
    v = int(input(f"Enter value for item {i+1}: "))
    values.append(v)

capacity = int(input("Enter Knapsack capacity: "))
max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")

