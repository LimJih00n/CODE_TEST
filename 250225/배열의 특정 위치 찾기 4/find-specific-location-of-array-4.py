arr = list(map(int,input().split()))
two = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    if arr[i]%2==0:
        two.append(arr[i])
print(len(two),sum(two))
    