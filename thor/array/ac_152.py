#! /usr/bin/env python

class Solution(object):
	def maxProduct1(self, nums: [int]) -> int:
		'''
			求数组中子区间的最大乘积，对于乘法，我们需要注意，负数乘以负数，会变成正数，所以我们需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。
			动态方程可能这样：

			maxDP[i + 1] = max(maxDP[i] * A[i + 1], A[i + 1],minDP[i] * A[i + 1])
			minDP[i + 1] = min(minDP[i] * A[i + 1], A[i + 1],maxDP[i] * A[i + 1])
			dp[i + 1] = max(dp[i], maxDP[i + 1])

			另外，还需要注意元素为0的情况，如果A[i]为0，那么maxDP和minDP都为0，
		:param nums:
		:return:
		'''
		if not nums:
			return -1
		else:
			p, max_p, min_p = nums[0], nums[0], nums[0]
			for i in range(1, len(nums)):
				temp = max_p
				max_p = max(max(max_p * nums[i], nums[i]), min_p * nums[i])
				min_p = min(min(temp * nums[i], nums[i]), min_p * nums[i])
				p = max(max_p, p)
			return p

	def maxProduct(self, nums: [int]) -> int:
		'''
			python超时了,java可以实现
		:param nums:
		:return:
		'''
		if not nums:
			return -1
		else:
			ans = nums[0]
			for i in range(1, len(nums)):
				for j in range(i):
					nums[j] = nums[j] * nums[i]
					ans = max(ans, max(nums[j], nums[i]))
			return ans


if __name__ == '__main__':
	s = Solution()
	print(s.maxProduct1([2, 3, -2, 4]))
	print(s.maxProduct1([-2, 0, -1]))
	print(s.maxProduct1([-4, -3]))
	print(s.maxProduct1([0, 2]))
	print(s.maxProduct1([3, -1, 4]))
