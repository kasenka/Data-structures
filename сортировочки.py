# пузырьковская

def buble(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# print(buble([1,4,2,6,4,7,0,12,1,1,1,4,3,56,9]))


def fast(arr):
    if len(arr) <= 1:  # Базовый случай: если массив пуст или содержит один элемент, он уже отсортирован
        return arr
    else:
        left = []
        right = []
        dot = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < dot: left.append(arr[i])
            else: right.append(arr[i])
        return fast(left) + [dot] + fast(right)

# print(fast([1,4,2,6,4,7,0,12,1,1,1,4,3,56,9]))

def stavka(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and (arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# print(stavka([1,4,2,6,4,7,0,12,1,1,1,4,3,56,9]))

def vibori(arr):
    for i in range(len(arr)):
        min_in = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_in]:
                min_in = j
        arr[i], arr[min_in] = arr[min_in], arr[i]
    return arr

print(vibori([1,4,2,6,4,7,0,12,1,1,1,4,3,56,9]))


