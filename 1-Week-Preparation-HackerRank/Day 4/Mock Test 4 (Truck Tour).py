# Function to find starting point where the truck can start to get through
# the complete circle without exhausting its petrol in between.
def tour(self, lis, n):
	# Code here
	curr_petro = start = 0
	prev_petro = 0
	for i in range(n):
		curr_petro += lis[i][0] - lis[i][1]
		if curr_petro < 0:
			prev_petro += curr_petro
			curr_petro = 0
			start = i + 1

	return start if (curr_petro + prev_petro) >= 0 else -1

# time: O(n), space: O(1)
