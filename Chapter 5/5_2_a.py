def check_ferma(a, b, c, n):
	if ((a**n) + (b**n)) != (c**n):
		print('아냐, 공식이 맞지 않아!')
	else:
		print('이럴 수가! 페르마가 틀렸어!')

check_ferma(3, 4, 5, 3)