a, b, c, d = map(int, input().split())

# Please write your code here.

tiem1 = a*60+b
time2 = c*60+d
m = 0
while True:
    tiem1 += 1
    m+=1
    if tiem1==time2:
        break
print(m)