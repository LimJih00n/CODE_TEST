cnt = 1
n = int(input())

for i in range(n):
    for j in range(i):
        print("  ",end="")
    for j in range(n-i,0,-1):
        print(cnt,end=" ")
        cnt = cnt +1 if cnt<9 else 1
    print()