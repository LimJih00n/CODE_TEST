arr = list(map(int,input().split()))

for n in range(len(arr)):
    if arr[n] == 0:
        idx = n
        break
arr = arr[0:idx]

print(arr[-1]+arr[-2]+arr[-3])
