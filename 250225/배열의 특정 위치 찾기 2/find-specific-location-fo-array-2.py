arr = list(map(int,input().split()))
num1 = sum(arr[1::2])
num2 = sum(arr[0::2])
print(abs(num1-num2))
