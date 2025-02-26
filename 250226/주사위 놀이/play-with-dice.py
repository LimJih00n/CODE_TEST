count = [0]*6
arr = list(map(int,input().split()))
for n in arr:
    count[n-1] +=1
for i in range(6):
    print(i+1,"-",count[i])