def is_triangle(n1, n2, n3):
	if (n1 > (n2 + n3) or n2 > (n1 + n3) or n1 > (n2 + n3)): 
		print('NO')
	else:
		print('YES')

is_triangle(3, 4, 5)
is_triangle(9, 4, 5)
is_triangle(10, 4, 5)
