A = input()
count = 0
for i in range(len(A)):
    if A[i] == "(":
        for j in range(i,len(A)):
            if A[j] == ")":
                count +=1
print(count)