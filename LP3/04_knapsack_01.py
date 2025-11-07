def knapsack_01(values, weights, capacity):
    n = len(values)
    
    # DP table initialization
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], 
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

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

max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value: {max_value}")