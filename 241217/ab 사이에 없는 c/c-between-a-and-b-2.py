a,b,c = map(int,input().split())
re = "YES"
for i in range(a,b+1):
    if i % c == 0:
        re = "NO"
print(re)
