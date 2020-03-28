import unittest
from unittest import TestCase

from thor.algorithmn.array_sort import ArraySort


class TestArraySort(TestCase):

	def test_selection_sort(self):
		result = ArraySort.selection_sort([2, 1, 3, 7])
		self.assertEqual([1, 2, 3, 7], result)
		result = ArraySort.selection_sort([])
		self.assertIsNone(result)
		result = ArraySort.selection_sort([1])
		self.assertEqual([1], result)
		result = ArraySort.selection_sort([1, 2])
		self.assertEqual([1, 2], result)

	def test_insertion_sort(self):
		result = ArraySort.insertion_sort([2, 1, 3, 7, 5])
		self.assertEqual([1, 2, 3, 5, 7], result)
		self.assertEqual(1, result[0])
		self.assertEqual(3, result[2])
		self.assertEqual(7, result[4])

	def test_merge_sort(self):
		result = ArraySort.merge_sort([23, 12, 145, 1])
		self.assertEqual([1, 12, 23, 145], result)
		result = ArraySort.merge_sort([])
		self.assertEqual([], result)
		result = ArraySort.merge_sort([1])
		self.assertEqual([1], result)
		result = ArraySort.merge_sort([1, 2])
		self.assertEqual([1, 2], result)


if __name__ == '__main__':
	unittest.main()
