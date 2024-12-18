n = int(input())


for i in range(10,10+n*2,2):
    for j in range(1,n*2,2):
        print(i+j,end=" ")
    print()
