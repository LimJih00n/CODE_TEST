n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*100
for x1,x2 in segments:
    for idx in range(x1,x2+1):
        arr[idx]+=1
print(max(arr))