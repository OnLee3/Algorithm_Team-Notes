data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# selection sort
for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

# insertion sort
for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j-1] < data[j]:
            data[j-1], data[j] = data[j], data[j-1]
        else:
            break

# quick sort


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in pivot if x <= pivot]
    right = [x for x in pivot if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# counting sort
count = [0]*(max(data)+1)
for i in data:
    count[i] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
