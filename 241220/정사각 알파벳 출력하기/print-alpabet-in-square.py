n = int(input())
cnt=0
for i in range(n):
    for j in range(n):
        print(chr(65+cnt),end="")
        cnt+=1
    print()