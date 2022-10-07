a, b, c = list(map(int, input().split()))

arr = input().split(' ')
arr = list(map(int, arr))

if len(arr) < 3:
    print("You have to enter bigger array")
    exit()

answer = []
for i in range(0, len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
        for k in range(j + 1, len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                answer.append((arr[i], arr[j], arr[k]))

print(len(answer))