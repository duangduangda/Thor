import unittest
from unittest import TestCase

from thor.interview.ac_3 import Solution


class TestSolution(TestCase):

	def test_exists_duplicate_nums_1(self):
		self.assertEqual(2, Solution.find_repeat_nums([2, 3, 1, 0, 2, 5, 3]))

	def test_exists_duplicate_nums_2(self):
		self.assertEqual(1, Solution.find_repeat_nums([1, 2, 3, 4, 1]))


if __name__ == '__main__':
	unittest.main()
