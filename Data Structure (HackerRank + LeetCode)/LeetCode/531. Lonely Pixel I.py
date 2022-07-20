from collections import defaultdict


class Solution:
	def findLonelyPixel(self, picture: List[List[str]]) -> int:
		m, n = len(picture), len(picture[0])
		rows, cols = [0] * m, [0] * n

		for i in range(m):
			for j in range(n):
				if picture[i][j] == 'B':
					rows[i] += 1
					cols[j] += 1
		print(rows)
		print(cols)
		count = 0
		for i in range(m):
			for j in range(n):
				if picture[i][j] == 'B':
					if rows[i] == 1 and cols[j] == 1:
						count += 1
		return count