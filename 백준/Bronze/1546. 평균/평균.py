n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
result = 0

for score in scores:
    result += (score / max_score) * 100

print(result / len(scores))