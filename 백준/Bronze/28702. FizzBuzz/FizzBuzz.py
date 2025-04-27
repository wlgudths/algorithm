def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

arr = []
idx = 3

for _ in range(3):
    arr.append((input(), idx))
    idx -= 1

for i, j in arr:
    if i.isdigit():
        ans = fizzbuzz(int(i) + j)
        break
    else:
        ans = 'any'

print(ans)