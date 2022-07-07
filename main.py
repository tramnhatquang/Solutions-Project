
if __name__ == '__main__':
	a = [1, 2, 4]
	b = a
	a[1] = 10
	print(b)

	c = a[:]
	print(c)

	c[1] = 100
	print(a, b)

	a[:] = c