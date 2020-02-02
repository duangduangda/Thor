#! /usr/bin/env python

'''
	线性扫描
'''


class Solution(object):
	'''
		1. 找出最大数
		2. 判断是否存在符合条件的数值
		3. 如果存在符合条件的数值，获取其下标，否则返回-1
	'''

	def dominantIndex(self, nums: [int]) -> int:
		if nums is None:
			return -1
		else:
			max_val = max(nums)
			flag = True

			for i in range(len(nums)):
				if nums[i] != max_val and nums[i] * 2 > max_val:
					flag = False
					break
			if not flag:
				return -1
			else:
				return nums.index(max_val)

	def dominantIndex1(self, nums: [int]) -> int:
		if nums is None:
			return -1
		else:
			max_val = max(nums)
			if all(max_val >= 2 * x for x in nums if x != max_val):
				return nums.index(max_val)
			else:
				return -1


if __name__ == '__main__':
	s = Solution()
	print(s.dominantIndex([3, 6, 1, 0]))
	print(s.dominantIndex([0, 0, 0, 1]))
	print(s.dominantIndex1([3, 6, 1, 0]))
	print(s.dominantIndex1([0, 0, 0, 1]))
