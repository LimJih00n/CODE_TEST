arr = list(map(int,input().split()))
idx = 9
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
print(sum(arr[0:idx+1]),round(sum(arr[0:idx])/(idx),1))