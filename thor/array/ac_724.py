# coding:utf-8

class Solution(object):
	"""
		1. 计算整个数组的和sum
		2. 如果存在中心索引，则left == right,因此可推算出left * 2 + nums[i] == sum，i为中心索引
		3. 如果不存在，返回-1
	"""

	def privotIndex(self, nums) -> int:
		if nums is None:
			return -1
		else:
			sum_val = sum(nums)
			for i in range(len(nums)):
				if i == 0:
					left = 0
				else:
					left += nums[i - 1]
				if left * 2 + nums[i] == sum_val:
					return i
			return -1


def main():
	s = Solution()
	nums = [1, 7, 3, 6, 5, 6]
	print(s.privotIndex(nums))
	nums = [1, 2, 3]
	print(s.privotIndex(nums))
	nums = [-1, -1, -1, -1, -1, 0]
	print(s.privotIndex(nums))
	print(s.privotIndex(nums = [1, 1]))


if __name__ == '__main__':
	main()
