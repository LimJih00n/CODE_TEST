a,b = map(int,input().split())

for i in range(1,10):
    for j in range(b,a-1,-2):
        
        if j ==a:
            print(f"{j} * {i} = {j*i} ",end="")
        else:
            print(f"{j} * {i} = {j*i} / ",end="")
    print()