count = [0]*10
n = int(input())
arr = list(map(int,input().split()))
for n in arr:
    count[n] +=1
for i in range(1,10):
    print(count[i])