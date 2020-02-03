#! /usr/bin/env python

class Solution(object):
	def search(self, nums: [int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left < right:
			mid = left + (right - left) // 2
			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid

		return left if nums[left] == target else -1

	def search1(self, nums: [int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if nums[mid] < target:
				left = mid + 1
			elif nums[mid] > target:
				right = mid - 1
			else:
				return mid
		return -1
