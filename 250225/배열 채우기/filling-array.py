arr = list(map(int,input().split()))
idx =len(arr)
for i in range(len(arr)):
    if arr[i]==0:
        idx = i
arr = arr[idx-1::-1]
print(*arr)