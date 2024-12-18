n = int(input())
cnt = 1
in_cnt=1

#1 1 2 3 4
#2 8 7 6 5
# n*2 - j
#3 9 10 11 12

for i in range(1,n+1):
    if i%2==1:
        for j in range(n):
            print(cnt,end=" ")
            cnt+=1
    else:
        for j in range(n):
            print(n*i-j,end=" ")
            cnt+=1
    print()