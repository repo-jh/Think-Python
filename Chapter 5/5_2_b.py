def check_ferma(a, b, c, n):
	if ((a**n) + (b**n)) != (c**n):
		print('아냐, 공식이 맞지 않아!')
	else:
		print('이럴 수가! 페르마가 틀렸어!')

temp_a = int(input('a의 값을 입력하세요.\n'))
temp_b = int(input('b의 값을 입력하세요.\n'))
temp_c = int(input('c의 값을 입력하세요.\n'))
temp_d = int(input('d의 값을 입력하세요.\n'))

check_ferma(temp_a, temp_b, temp_c, temp_d)
