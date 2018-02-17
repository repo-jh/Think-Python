import turtle, math

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

"""
def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon(t, length, n)
"""
def circle(t, r):
	circumference = 2 * math.pi * r
	n = int(circumference / 3) + 1 
	print(n)
	length = circumference / n
	polygon(t, length, n)

bob = turtle.Turtle()
print(bob)
circle(bob, 100)
turtle.mainloop()
