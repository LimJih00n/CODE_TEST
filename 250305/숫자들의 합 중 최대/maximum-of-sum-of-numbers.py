a,b = input().split()
ans = float('-inf')
for n in range(int(a),int(b)+1):
    tot = 0
    for c in str(n):
        tot += int(c)
    ans = max(ans,tot)
print(ans)