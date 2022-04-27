import math
import random
import unittest

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

class TestProgram(unittest.TestCase):
	def test_case_1_bubble_sort(self):
		input_1 = [3, 4, 1, 5, -1, 2, 3]
		expected_1 = [-1, 1, 2, 3, 3, 4, 5]
		self.assertEqual(bubble_sort(input_1), expected_1)

	def test_case_2_bubble_sort(self):
		input_2 = [3, 3, 3]
		expected_2 = [3, 3, 3]
		self.assertEqual(bubble_sort(input_2), expected_2)

	def test_case_3_bubble_sort(self):
		input_3 = []
		expected_3 = []
		self.assertEqual(bubble_sort(input_3), expected_3)

	def test_case_4_bubble_sort(self):
		input_1 = [1, 2, 3, 4]
		expected_1 = [1, 2, 3, 4]
		self.assertEqual(bubble_sort(input_1), expected_1)

	def test_case_5_bubble_sort(self):
		input_1 = []
		for i in range(10000):
			input_1.append(random.randint(1, 100))
		self.assertEqual(bubble_sort(input_1), sorted(input_1))

	def test_case_6_bubble_sort(self):
		self.assertEqual(bubble_sort([1]), [1])

	# --------------------------------------------------------------------------
	def test_case_1_selection_sort(self):
		input_1 = [3, 4, 1, 5, -1, 2, 3]
		expected_1 = [-1, 1, 2, 3, 3, 4, 5]
		self.assertEqual(selection_sort(input_1), expected_1)

	def test_case_2_selection_sort(self):
		input_2 = [3, 3, 3]
		expected_2 = [3, 3, 3]
		self.assertEqual(selection_sort(input_2), expected_2)

	def test_case_3_selection_sort(self):
		input_3 = []
		expected_3 = []
		self.assertEqual(selection_sort(input_3), expected_3)

	def test_case_4_selection_sort(self):
		input_1 = [1, 2, 3, 4]
		expected_1 = [1, 2, 3, 4]
		self.assertEqual(selection_sort(input_1), expected_1)

	def test_case_5_selection_sort(self):
		input_1 = []
		for i in range(10000):
			input_1.append(random.randint(1, 100))
		self.assertEqual(selection_sort(input_1), sorted(input_1))

	def test_case_6_selection_sort(self):
		self.assertEqual(selection_sort([1]), [1])

# --------------------------------------------------------------------------
	def test_case_1_merge_sort(self):
		input_1 = [3, 4, 1, 5, -1, 2, 3]
		expected_1 = [-1, 1, 2, 3, 3, 4, 5]
		self.assertEqual(merge_sort(input_1), expected_1)

	def test_case_2_merge_sort(self):
		input_2 = [3, 3, 3]
		expected_2 = [3, 3, 3]
		self.assertEqual(merge_sort(input_2), expected_2)

	def test_case_3_merge_sort(self):
		input_3 = []
		expected_3 = []
		self.assertEqual(merge_sort(input_3), expected_3)

	def test_case_4_merge_sort(self):
		input_1 = [1, 2, 3, 4]
		expected_1 = [1, 2, 3, 4]
		self.assertEqual(merge_sort(input_1), expected_1)

	def test_case_5_merge_sort(self):
		input_1 = []
		for i in range(1000000):
			input_1.append(random.randint(1, 100))
		self.assertEqual(merge_sort(input_1), sorted(input_1))

	def test_case_6_merge_sort(self):
		self.assertEqual(merge_sort([1]), [1])

	# --------------------------------------------------------------------------
	def test_case_1_quick_sort(self):
		input_1 = [3, 4, 1, 5, -1, 2, 3]
		expected_1 = [-1, 1, 2, 3, 3, 4, 5]
		self.assertEqual(quick_sort(input_1), expected_1)

	def test_case_2_quick_sort(self):
		input_2 = [3, 3, 3]
		expected_2 = [3, 3, 3]
		self.assertEqual(quick_sort(input_2), expected_2)

	def test_case_3_quick_sort(self):
		input_3 = []
		expected_3 = []
		self.assertEqual(quick_sort(input_3), expected_3)

	def test_case_4_quick_sort(self):
		input_1 = [1, 2, 3, 4]
		expected_1 = [1, 2, 3, 4]
		self.assertEqual(quick_sort(input_1), expected_1)

	def test_case_5_quick_sort(self):
		input_1 = []
		for i in range(10000):
			input_1.append(random.randint(1, 100))
		self.assertEqual(quick_sort(input_1), sorted(input_1))

	def test_case_6_quick_sort(self):
		self.assertEqual(quick_sort([1]), [1])


if __name__ == '__main__':
	unittest.main()
