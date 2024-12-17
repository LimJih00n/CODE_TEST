n = int(input())
re = "P"

for i in range(2,n):
    if n % i ==0:
        re="C"
print(re)