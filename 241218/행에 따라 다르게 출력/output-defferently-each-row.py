cnt = 1
n = int(input())
for i in range(n):
    for j in range(n):
        print(cnt,end=" ")
        cnt = cnt + 1 if i%2==0 else cnt +2
    print()