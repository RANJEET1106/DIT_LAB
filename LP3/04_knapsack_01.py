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

values  = [50,100,150,200]
weights = [8,16,32,40]
capacity = 64

max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value: {max_value}")