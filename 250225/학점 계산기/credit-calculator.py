N = int(input())
arr = list(map(float,input().split()))
score = round(sum(arr)/N,1)
print(score)
if score >=4:
    print("Perfect")
elif score >=3:
    print("Good")
else:
    print("Poor")

