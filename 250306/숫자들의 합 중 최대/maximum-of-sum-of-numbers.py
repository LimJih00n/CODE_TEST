'''
입력
x,y

what : x,y 사이의 수를 순회하면서 자릿수를 모두 더하고 그게 최대일때의  그 값=> 합의 값

how: x,y 순회 -> 자릿수 분해해서 더하기 -> 크면 저장하기
'''
X,Y =map(int, input().split())
max_num = float('-inf')
ans = X
for i in range(X,Y+1):
    if max_num<sum(list(map(int,str(i)))):
        max_num =sum(list(map(int,str(i))))
        
print(max_num)

    

