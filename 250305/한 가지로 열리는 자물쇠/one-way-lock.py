N = int(input())
a,b,c = map(int,input().split())
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if  (i-2 <= a <= i+2 or j-2 <= b <= j+2 or k-2 <= c <= k+2):
                ans +=1
print(ans)
