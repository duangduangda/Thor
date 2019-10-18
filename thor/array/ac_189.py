# coding:utf-8


class Solution(object):
	def rotate1(self, nums, k) -> None:
		"""
			使用
		:param nums:
		:param k:
		:return:
		"""
		length = len(nums)
		if nums is None or length == 1 or k == 0:
			return None
		else:
			results = nums[:]
			for i in range(length):
				nums[(i + k) % length] = results[i]

	def rotate(self, nums, k):
		length = len(nums)
		"""防止K值超过length"""
		k %= length
		self.reverse(nums, 0, length - 1)
		self.reverse(nums, 0, k - 1)
		self.reverse(nums, k, length - 1)
		travel(nums)

	def reverse(self, nums, m, n):
		while m < n:
			nums[m], nums[n] = nums[n], nums[m]
			m += 1
			n -= 1


def travel(nums):
	for i in nums:
		print(i, end = "")
	print()


def main():
	s = Solution()
	s.rotate(nums = [1, 2, 3, 4, 5], k = 2)


if __name__ == '__main__':
	main()
