#! /usr/bin/env python

'''
	1. 变化前和变化的位数是一样的
		1.1 加完后，值不小于10，需要做进位
			1.1.1 进位后，首位数字不小于10，位数将增加1
			1.1.2 进位后，首位数字小于10
		1.2 加完后，值小于10

'''


class Solution(object):
	def plusOne(self, digits: [int]) -> [int]:
		'''
			字符串和数值之间的转化
		:param digits:
		:return:
		'''
		if not digits:
			return digits
		else:
			return [int(x) for x in str(int(''.join(str(i) for i in digits)) + 1)]

	def plusOneExtend(self, digits: [int]) -> [int]:
		'''
			进位计算
		:param digits:
		:return:
		'''
		i = len(digits) - 1
		while i >= 0:
			digits[i] = digits[i] + 1
			digits[i] = digits[i] % 10
			if digits[i] != 0:
				return digits
			i = i - 1
		return [1] + digits


if __name__ == '__main__':
	s = Solution()
	print(s.plusOne([1, 2, 3]))
	print(s.plusOne([9]))
	print(s.plusOneExtend([1, 2, 3]))
	print(s.plusOneExtend([9]))
