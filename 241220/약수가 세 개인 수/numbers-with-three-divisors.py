s,e = map(int,input().split())
cc=0
for i in range(s,e+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    
    if cnt == 3:
        cc +=1
print(cc)