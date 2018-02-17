def do_twice(func, s):
    func(s)
    func(s)

def print_twice(s):
    print(s)
    print(s)

def do_four(func, s):
    do_twice(func, s)
    do_twice(func, s)

do_four(print_twice, 'spam')
