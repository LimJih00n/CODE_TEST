n = int(input())
count = 0
arr = []
i=1
while True:
    
    if (n*i) %5 == 0:
        count += 1
    
    arr.append(n*i)
    i+=1
    if count ==2:
        break
  
print(*arr)