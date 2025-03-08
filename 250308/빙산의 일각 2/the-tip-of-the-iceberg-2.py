'''
what? 물의 높이를 적절하게 설정했을대 남기는 빙산덩어리의 최대값을 구하기
빙산덩어리 => 연결되지 않은 거의 최대
연결 => 좌우로 양수로 연속되면 연결
=> 연속되지 않은 양수의 최대 count를 구하는 것.

how?
값들 1씩 빼고 빙산 count 
빙산 count => 연속하는 양수의 수 count
1 1 0 1 2 => 2
0 1 0 1 0 1 => 3
필요변수: 연속중임을 나타내는 것, 얼마나 연속했는지 나타내는 것.
'''

def cal_iceage(arr):
    seq_count = False
    re = 0
    for i in range(len(arr)):
        if not seq_count and arr[i]>0: #연속하는 것의 개수를 구하는 것
        # 얼마나 연속하는지는 알필요 없다. 
            seq_count = True
            re += 1
        if arr[i]<=0:
            seq_count = False
    return re
N = int(input())
iceage = [int(input()) for i in range(N)]

ans = 0
min_h = min(iceage)
max_h = max(iceage)
for i in range(max_h+1):
    new_age = [n-i for n in iceage]
    ans = max(ans,cal_iceage(new_age))
print(ans)
