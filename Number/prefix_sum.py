def prefix_sum(n, m, data):
    dp = [0]
    data_sum = 0
    for i in range(n):
        data_sum += data[i]
        dp.append(data_sum)
    return dp[m[1]] - dp[m[0]-1]


print(prefix_sum(5, (2, 4), [10, 20, 30, 40, 50]))
