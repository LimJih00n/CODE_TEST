n = int(input())

for r in range(n):
    for c in range(n):
        if r == 0 or c==0 or r==n-1 or c==n-1:
            print("* ",end="")
        elif r>c:
            print("* ",end="")
        else:
            print("  ",end="")
    print()