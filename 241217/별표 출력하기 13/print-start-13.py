n = int(input())

for i in range(n*2):
    if i%2 == 0:
        print("* "*(n-i//2))
    else:
        print("* "*(i//2+1))