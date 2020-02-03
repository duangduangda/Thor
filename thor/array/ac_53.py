#! /usr/bin/env python

'''
	最大子序列和:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
'''


class Solution(object):
	def maxSubArray(self, nums: [int]) -> int:
		'''
			贪心.使用单个数组作为输入来查找最大（或最小）元素（或总和）的问题，贪心算法是可以在线性时间解决的方法之一。
每一步都选择最佳方案，到最后就是全局最优的方案。
		:param nums:
		:return:
		'''
		if not nums:
			return -1
		else:
			max_sum = nums[0]
			sum = 0
			for num in nums:
				if sum > 0:
					# append
					sum = sum + num
				else:
					# clear and reset
					sum = num
				max_sum = max(max_sum, sum)
			return max_sum

	def maxSubArray1(self, nums: [int]) -> int:
		'''
			动态规划。 在整个数组或在固定大小的滑动窗口中找到总和或最大值或最小值的问题可以通过动态规划（DP）在线性时间内解决。
			有两种标准 DP 方法适用于数组：
			1. 常数空间，沿数组移动并在原数组修改。
			2. 线性空间，首先沿 left->right 方向移动，然后再沿 right->left 方向移动。 合并结果
		:param nums:
		:return:
		'''
		n = len(nums)
		max_sum = nums[0]
		for i in range(1, n):
			if nums[i - 1] > 0:
				nums[i] += nums[i - 1]
			max_sum = max(nums[i], max_sum)
		return max_sum


if __name__ == '__main__':
	s = Solution()
	print(s.maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
