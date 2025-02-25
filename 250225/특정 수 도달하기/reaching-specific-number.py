tot = 0
count = True
arr1 = list(map(int,input().split()))
arr=[]
for i in range(10):
    
    if arr1[i]<250 and count:
        arr.append(arr1[i])
    else:
        count = False

print(sum(arr),round(sum(arr)/len(arr),1))
    
