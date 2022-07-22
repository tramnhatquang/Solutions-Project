def findZigZagSequence(a, n):
	a.sort()
	mid = (n // 2)  # change this line
	a[mid], a[n - 1] = a[n - 1], a[mid]

	st = mid + 1
	ed = n - 2  # change this line
	while (st <= ed):
		a[st], a[ed] = a[ed], a[st]
		st = st + 1
		ed = ed - 1  # change this line to decrement

	for i in range(n):
		if i == n - 1:
			print(a[i])
		else:
			print(a[i], end=' ')
	return


test_cases = int(input())
for cs in range(test_cases):
	n = int(input())
	a = list(map(int, input().split()))
	findZigZagSequence(a, n)
