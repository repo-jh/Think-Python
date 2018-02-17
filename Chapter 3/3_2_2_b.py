def do_twice(func, s):
	func()
	func()

def print_spam():
	print('spam ')

do_twice(print_spam, '')
