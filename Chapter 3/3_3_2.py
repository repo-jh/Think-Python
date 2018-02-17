def print_hl_1():
	print('+', '- '*4, end='')
	print('+', '- '*4, end='')
	print('+', '- '*4, end='')
	print('+', '- '*4, end='')
	print('+')

def print_h1_2():
	print('|', ' '*7, '|', ' '*7, '|', ' '*7, '|', ' '*7, '|')

def do_four(func):
	do_twice(func)
	do_twice(func)

def do_twice(func):
	func()
	func()

def do_draw():
	do_four(print_h1_2)
	print_hl_1()

print_hl_1()
do_draw()
do_draw()
do_draw()
do_draw()
