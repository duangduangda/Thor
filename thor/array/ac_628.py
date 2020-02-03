#! /usr/bin/env python

'''
	给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
'''


class Solution(object):
	def maximumProduct(self, nums: [int]) -> int:
		'''
			降序排序后结果只可能是前三个数乘积或者第一个正数和最后两个负数乘积
		:param nums:
		:return:
		'''
		if not nums or len(nums) < 3:
			return 0
		else:
			nums = sorted(nums, reverse = True)
			return max(nums[-1] * nums[-2] * nums[1], nums[0] * nums[1] * nums[2])

	def maximumProduct1(self, nums: [int]) -> int:
		'''
			寻找三个最大数和两个最小数，比较三个最大数乘积和两个最小数和一个最大数乘积。
		:param nums:
		:return:
		'''
		max1, max2, max3, min1, min2 = -1000, -1000, -1000, 1000, 1000
		for num in nums:
			if num <= min1:
				min2 = min1
				min1 = num
			elif num <= min2:
				min2 = num
				
			if num >= max1:
				max3 = max2
				max2 = max1
				max1 = num
			elif num >= max2:
				max2 = max1
				max1 = num
			elif num >= max3:
				max3 = num
		return max(min1 * min2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
	s = Solution()
	print(s.maximumProduct([1, 2, 3]))
	print(s.maximumProduct([1, 2, 3, 4]))
	print(s.maximumProduct([2, 2, 2, 3]))
	print(s.maximumProduct1([1, 2, 3]))
	print(s.maximumProduct1([1, 2, 3, 4]))
	print(s.maximumProduct1([2, 2, 2, 3]))
