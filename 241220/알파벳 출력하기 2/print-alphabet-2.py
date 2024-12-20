n = int(input())
cnt = 0

for i in range(n):
    for j in range(i):
        print("  ",end="")
    for j in range(n-i):
        print(chr(65+cnt),end=" ")
        cnt = cnt+1 if chr(cnt+65) !="Z" else 0
    print()