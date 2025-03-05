n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
mean = sum(arr)/n
ans = 0
for i in range(n):
    tot_arr = []
    for j in range(i,n):
        
        tot_arr.append(arr[j])
    
        m_tot = sum(tot_arr)/len(tot_arr)
        ans = ans+1 if m_tot in tot_arr else ans
print(ans)
