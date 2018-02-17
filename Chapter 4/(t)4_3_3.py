import turtle

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

bob = turtle.Turtle()
print(bob)
polygon(bob, 50, 8)
turtle.mainloop()
