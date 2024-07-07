# N 입력 받기
n = int(input())
# N개의 정수, 가게가 보유한 부품 입력 받기
store = list(map(int, input().split()))

# M 입력 받기
m = int(input())
# M개의 정수, 손님이 요청하는 부품 입력 받기
customer = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return True
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return False

start = 0
end = len(store) - 1

for i in customer:
    if binary_search(store, i, start, end) == True:
        print('yes', end=' ')
    else:
        print('no', end =' ')

