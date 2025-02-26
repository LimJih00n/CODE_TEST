per = []
hes = [0]*4
for i in range(3):
    per.append(list(input().split()))
for v in per:
    if int(v[1])>=37 and v[0]=='Y':
        hes[0]+=1
    elif int(v[1])>=37 and v[0]=='N':
        hes[1]+=1
    elif int(v[1])<37 and v[0]=='Y':
        hes[2]+=1
    else:
        hes[3]+=1
if hes[0]>=2:
    hes.append("E")
for n in hes:
    print(n,end=" ")

