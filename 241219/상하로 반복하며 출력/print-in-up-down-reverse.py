n = int(input())
# 1 4 1 4
# 2 3 2 3
# 3 2 3 2
# 4 1 4 1
cnt = 1
for i in range(n):
    for j in range(n):
        if j%2==0:
            print(cnt,end="")
        else:
            print(n-cnt+1,end="")
    cnt+=1
    print()