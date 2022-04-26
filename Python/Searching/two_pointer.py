def two_pointer(n, m, data):
    end = 0
    cnt = 0
    interval_sum = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1
        if interval_sum == m:
            cnt += 1
        interval_sum -= data[start]
    return cnt


print(two_pointer(5, 5, [1, 2, 3, 2, 5]))
