#! /usr/bin/env python
'''
	给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
	函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
'''


class Solution(object):
	def twoSum(self, numbers: [int], target: int) -> [int]:
		'''

			使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。

			1. 如果两个指针指向元素的和 sum == targetsum==target，那么得到要求的结果；
			2. 如果 sum > targetsum>target，移动较大的元素，使 sumsum 变小一些；
			3. 如果 sum < targetsum<target，移动较小的元素，使 sumsum 变大一些。
			数组中的元素最多遍历一次，时间复杂度为 O(N)O(N)。只使用了两个额外变量，空间复杂度为 O(1)O(1)。
		:param numbers:
		:param target:
		:return:
		'''
		result = []
		if not numbers:
			return result
		slow, fast = 0, len(numbers) - 1
		while slow < fast:
			if numbers[slow] == target - numbers[fast]:
				return [slow + 1, fast + 1]
			elif numbers[slow] < target - numbers[fast]:
				slow = slow + 1
			else:
				fast = fast - 1
		return result


if __name__ == '__main__':
	s = Solution()
	print(s.twoSum([2, 7, 11, 25], 9))
	print(s.twoSum([2, 6, 7], 9))
	print(s.twoSum([2, 3, 4], 6))
	print(s.twoSum([-1, 0], -1))
