N = int(input())
arr = list(map(int,input().split()))
ans = []
for num in arr:
    if num %2 == 0:
        ans.append(num)
print(*ans[::-1])