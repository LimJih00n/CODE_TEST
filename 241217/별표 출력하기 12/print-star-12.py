n = int(input())
for r in range(n):
    for c in range(n):
        if r ==0:
            print("* ",end="")
        elif c %2 !=0 and c>=r:
            print("* ",end="")
        else:
            print("  ",end="")
    print()