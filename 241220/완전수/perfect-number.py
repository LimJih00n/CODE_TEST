s,e = map(int,input().split())


cnt=0
for i in range(s,e+1):
    sum_=0
    for j in range(1,i):
        if i%j == 0:
            sum_ += j
    if sum_ == i:
        cnt +=1
print(cnt)

