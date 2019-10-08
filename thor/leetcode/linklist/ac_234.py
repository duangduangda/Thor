# coding:utf-8
from thor.leetcode.linklist.ListNode import ListNode


class Solution(object):
	def isPalindrome(self, head: ListNode) -> bool:
		"""
			1. 使用快慢指针，先找到链表的中间结点
			2. 反转链表的前半部分
			3. 回文校验
		:param head:
		:return:
		"""
		if not head:
			return True
		slow = head
		fast = head.next
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		cur = slow.next
		slow.next = None
		p = None
		while cur:
			q = cur.next
			cur.next = p
			p = cur
			cur = q

		while p and head:
			if p.val != head.val:
				return False
			p = p.next
			head = head.next
		return True

	def isPalindrome1(self, head: ListNode) -> bool:
		"""使用数学方法"""
		x = 0
		y = 0
		delta = 1

		while head:
			x = x * 10 + head.val
			y = y + delta * head.val
			delta *= 10
			head = head.next
		return x == y
