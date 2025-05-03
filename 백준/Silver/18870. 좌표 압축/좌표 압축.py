import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
comparison = sorted(set(x))

mapping = {v: i for i, v in enumerate(comparison)}

print(' '.join(str(mapping[i]) for i in x))