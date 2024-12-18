cnt = 0
n = int(input())
for i in range(n):
    for j in range(n):
        cnt = cnt + 1 if i%2==0 else cnt +2
        print(cnt,end=" ")

        
    print()