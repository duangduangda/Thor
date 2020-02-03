#! /usr/bin/env python

'''
	给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
	假定数组中没有重复的元素.
	1. 有序数组可以采用二分查找法
	2. 如果找到了，直接返回mid
	3. 如果没有找到，递归到左右两个部分
'''


class Solution(object):
	def searchInsert(self, nums: [int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if target > nums[mid]:
				left = mid + 1
			elif target < nums[mid]:
				right = mid - 1
			else:
				return mid
		# if target <= nums[mid]:
		# 	return mid
		# else:
		# 	return mid + 1
		return left


if __name__ == '__main__':
	s = Solution()
	print(s.searchInsert([1, 3, 5, 6], 5))
	print(s.searchInsert([1, 3, 5, 6], 2))
	print(s.searchInsert([1, 3, 5, 6], 4))
	print(s.searchInsert([1, 3, 5, 6], 7))
	print(s.searchInsert([1, 3, 5, 6], 0))
