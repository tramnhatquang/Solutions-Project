def is_isomorphic(str_1: str, str_2: str) -> bool:
	# WRITE YOUR BRILLIANT CODE HERE
	if len(str_1) != len(str_2):
		return False
	map_str1_str2 = {}
	map_str2_str1 = {}

	for c1, c2 in zip(str_1, str_2):
		if c1 not in map_str1_str2 and c2 not in map_str2_str1:
			map_str1_str2[c1] = c2
			map_str2_str1[c2] = c1
		elif map_str1_str2.get(c1) != c2 or map_str2_str1.get(c2) != c1:
			return False

	return True

