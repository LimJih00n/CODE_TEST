arr=[]
for i in range(5):
    arr.append(int(input()))
re = 1
for n in arr:
    if n%3 !=0:
        re=0
print(re)