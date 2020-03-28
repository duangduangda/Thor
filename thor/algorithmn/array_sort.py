#! /usr/bin/env python


class ArraySort(object):

	@staticmethod
	def insertion_sort(elements: [int]) -> [int]:
		"""
			插入排序的特点是：采用增量的设计思路，每次要即将插入的子序列都是一个已经排好序的子序列，插入排序包含两个主要动作
			1. 寻找要插入的位置 2. 向后移动比目标值大或者小的元素
		:param elements: 待排序的序列
		:return: 已排好序的序列
		"""
		if not elements:
			return None
		else:
			for i in range(1, len(elements)):
				# 上一个已排好序的子序列的最后一位
				j = i - 1
				key = elements[i]
				while elements[j] > key and j >= 0:
					# 比key大的数值往后移动
					elements[j + 1] = elements[j]
					# 逆序往前继续比较
					j -= 1
				elements[j + 1] = key
			return elements

	@staticmethod
	def selection_sort(elements: [int]) -> [int]:
		"""
			选择排序的特点是将查找第n大的值将其放在索引为n的位置，每次交换一对元素，它们当中至少有一个将被移到其最终位置上;
			首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
		:param elements:
		:return:
		"""
		if not elements:
			return None
		else:
			size = len(elements)
			for i in range(0, size):
				key = elements[i]
				j = i + 1
				# 2 1 3 7 5
				while j < size:
					if elements[j] < key:
						temp = elements[j]
						elements[j] = key
						key = temp
					j += 1
				elements[i] = key
			return elements

	@staticmethod
	def merge_sort(elements):
		if len(elements) <= 1:
			return elements
		mid = len(elements) // 2
		left = elements[:mid]
		right = elements[mid:]
		left = ArraySort.merge_sort(left)
		right = ArraySort.merge_sort(right)
		return ArraySort.merge(left, right)

	@staticmethod
	def merge(left, right):
		result = []
		while left and right:
			if left[0] <= right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		if left:
			result += left
		if right:
			result += right

		return result
