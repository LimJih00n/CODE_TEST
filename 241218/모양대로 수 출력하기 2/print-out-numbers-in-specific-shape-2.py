n = int(input())

cnt = 2

for i in range(n):
    for j in range(n):
        print(cnt,end=" ")
        cnt = cnt +2 if cnt<8 else 2
    print()
