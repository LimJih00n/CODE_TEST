n = int(input())

for i in range(2,n+1):
    is_so = True
    for j in range(2,i):
        if i%j == 0:
            is_so =False
    if is_so and n!=1:
        print(i,end=" ")