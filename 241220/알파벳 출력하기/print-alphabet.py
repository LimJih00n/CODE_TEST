cnt = 0
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(chr(65+cnt),end="")
        cnt+=1
    print()