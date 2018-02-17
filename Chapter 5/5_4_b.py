def recurse(n, s):
"""
재귀함수 기능 : n은 매 반복 시 1씩 차감,
그리고 n과 s의 합은 다음 호출 시 전달됨
n의 값이 0이 되면 누적된 s의 값을 프린트 하고 종료됨
"""
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)

recurse(3, 0)
