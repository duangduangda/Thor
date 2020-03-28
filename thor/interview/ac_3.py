#! /usr/bin/env python
# --coding:utf8--

class Solution(object):
	def findRepeatNums1(self, nums: [int]) -> int:
		if not nums:
			return -1
		i = 0
		while i < len(nums):
			if nums[i] == i:
				i += 1
				continue
			if nums[nums[i]] == nums[i]:
				return nums[i]
			nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
		return -1

	def findRepeatNums(self, nums: [int]) -> int:
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
