n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(i+j+65),end="")
    print()