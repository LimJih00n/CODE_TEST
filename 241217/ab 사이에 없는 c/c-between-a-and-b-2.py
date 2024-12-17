a,b,c = map(int,input().split())
re = "NO"
for i in range(a,b+1):
    if c % i == 0:
        re = "YES"
print(re)
