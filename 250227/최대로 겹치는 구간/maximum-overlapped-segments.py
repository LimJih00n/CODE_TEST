n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*201
for x1,x2 in segments:
    for idx in range(x1+100,x2+100):
        
        arr[idx] +=1
        
print(max(arr))
