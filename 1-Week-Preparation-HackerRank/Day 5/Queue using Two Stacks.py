# Enter your code here. Read input from STDIN. Print output to STDOUT

num_queries = int(input())
stack_push = []
stack_delete = []
for i in range(num_queries):
	query = list(input().strip().split())
	if query[0] == '1':
		stack_push.append(query[1])
	elif query[0] == '2':
		if not stack_delete:
			while stack_push:
				stack_delete.append(stack_push.pop())
		stack_delete.pop()
	else:
		# query[0] == '3'
		if not stack_delete:
			print(stack_push[0])
		else:
			print(stack_delete[-1])
