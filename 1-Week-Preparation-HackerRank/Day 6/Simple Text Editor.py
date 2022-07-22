# Enter your code here. Read input from STDIN. Print output to STDOUT
stack = []
string = ""
for _ in range(int(input())):
	t = input().split()

	if t[0] == '1':
		stack.append(string)
		string += t[1]
	elif t[0] == '2':
		stack.append(string)
		string = string[:-int(t[1])]
	elif t[0] == '3':
		print(string[int(t[1]) - 1])
	else:
		string = stack.pop()
