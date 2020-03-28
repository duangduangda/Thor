from unittest import TestCase

from thor.interview.ac_3 import Solution


class TestSolution(TestCase):

	def setUp(self):
		self.solution = Solution()

	def test_exists_duplicate_nums_1(self):
		self.assertEqual(2, self.solution.findRepeatNums([2, 3, 1, 0, 2, 5, 3]))

	def test_exists_duplicate_nums_2(self):
		self.assertEqual(1, self.solution.findRepeatNums([1, 2, 5, 4, 1]))
