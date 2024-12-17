n = int(input())

for i in range(n*2):
    if i%2==0:
        print("* "*((i//2)+1))
    else:
        print("* "*((n)-i//2))