#! /usr/bin/env python
# --coding:utf8--

"""
	在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""


class Solution(object):
	@staticmethod
	def find_repeat_nums(nums: [int]) -> int:
		"""
				对于这种数组元素在 [0, n-1] 范围内的问题，可以将值为 i 的元素调整到第 i 个位置上进行求解
		:param nums:
		:return:
		"""
		if not nums:
			return -1
		else:
			i = 0
			while i < len(nums):
				if nums[i] == i:
					i += 1
					continue
				if nums[nums[i]] == nums[i]:
					return nums[i]
				nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
			return -1

	@staticmethod
	def find_repeat_nums_v1(nums: [int]) -> int:
		if not nums:
			return -1
		element = {}
		for num in nums:
			if num not in element:
				element[num] = 1
			else:
				return num
		else:
			return -1
