def binary_search(lst, value):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == value:
            return 1
        elif lst[mid] < value:
            first = mid + 1
        else:
            last = mid - 1
    
    return 0

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    print(binary_search(n_list, num))

