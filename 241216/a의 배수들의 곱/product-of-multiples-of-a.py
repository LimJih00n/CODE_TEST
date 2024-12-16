a,b = map(int,input().split())
c = 1
for i in range(1,b+1):
    c *=  i if i%a==0 else 1
print(c)