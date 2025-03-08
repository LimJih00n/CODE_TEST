# 변수 선언 및 입력
n = int(input())
arr = [
	tuple(map(int, input().split()))
	for _ in range(n)
]

# 모든 숫자를 다 만들어 봅니다. (백의 자리수가 i, 십의 자리수가 j, 일의 자리수가 k)
cnt = 0
for i in range(1, 10):
	for j in range(1, 10):
		for k in range(1, 10):
			# 같은 수가 있는지 확인합니다.
			if i == j or j == k or k == i:
				continue
			
			# 해당 숫자가 정답일때, 모든 입력에 대해 올바른 답이 나왔는지 확인합니다.
			succeeded = True
			for a, num_cnt1, num_cnt2 in arr:
				# x : a[q]의 백의 자릿수, y : 십의 자릿수, z : 일의 자릿수
				x = a // 100
				y = a // 10 % 10
				z = a % 10
				
				# cnt1 : 1번 카운트, cnt2 : 2번 카운트
				cnt1 = 0
				cnt2 = 0
				if x == i:
					cnt1 += 1
				if y == j:
					cnt1 += 1
				if z == k:
					cnt1 += 1
				if x == j or x == k:
					cnt2 += 1
				if y == i or y == k:
					cnt2 += 1
				if z == i or z == j:
					cnt2 += 1

				# 만약 카운트 수가 다르다면 해당 숫자는 정답이 될 수 없습니다.
				if cnt1 != num_cnt1 or cnt2 != num_cnt2:
					succeeded = False
					break
			
			if succeeded:
				cnt += 1
    
print(cnt)
