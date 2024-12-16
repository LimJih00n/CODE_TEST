cnt = 0
n = int(input())
for i in range(1,n):
    if i%4 == 0:
        if not(n%100 ==0 and n%400 == 0):
            cnt+=1
print(cnt)