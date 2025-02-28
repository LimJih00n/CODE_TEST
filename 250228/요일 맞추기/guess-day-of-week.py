m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
start = 0
dir_=1
if m1 > m2:
    dir_ = -1
elif m1==m2:
    if d1>d2:
        dir_ = -1


while True:
    if m1 == m2 and d1 == d2:
        break
    d1 += dir_
    if mon[m1-1] > d1 and dir_>0:
        d1 = 1
        m1 +=1
    if d1 == 0 and dir_<0:
        m1 -= 1
        d1 = mon[m1-1]
    

    if dir_>0:
        start  = start+1 if start <7 else 0
    else:
        start  = start-1 if start > 0 else 6
print(days[start])