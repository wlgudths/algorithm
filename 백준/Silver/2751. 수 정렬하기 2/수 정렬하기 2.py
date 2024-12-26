def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= high:
        temp.append(arr[j])
        j += 1
    
    for k in range(low, high + 1):
        arr[k] = temp[k - low]
    
    return arr

def merge_sort(arr, low, high):
    if (low >= high):
        return arr
    
    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    sorted_array = merge(arr, low, high)

    return sorted_array


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = merge_sort(arr, 0, len(arr) - 1)

for i in arr:
    print(i)