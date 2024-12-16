cnt = 0
for i in range(10):
    a = int(input())
    cnt += 1 if a % 2 == 1 else 0
print(cnt)