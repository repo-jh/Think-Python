def is_triangle(n1, n2, n3):
	if (n1 > (n2 + n3) or n2 > (n1 + n3) or n1 > (n2 + n3)): 
		print('NO')
	else:
		print('YES')

t1 = int(input('n1 값을 입력하세요.\n'))
t2 = int(input('n2 값을 입력하세요.\n'))
t3 = int(input('n3 값을 입력하세요.\n'))
is_triangle(t1, t2, t3)
