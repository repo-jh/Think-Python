def do_twice(func, s):
	func(s)
	func(s)

def print_twice(s):
	print(s)
	print(s)

do_twice(print_twice, 'spam')
