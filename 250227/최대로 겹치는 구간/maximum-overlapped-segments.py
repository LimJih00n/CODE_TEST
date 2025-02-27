n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*202
for x1,x2 in segments:
    for idx in range(x1+100,x2+101):
        arr[idx] +=1
print(max(arr))