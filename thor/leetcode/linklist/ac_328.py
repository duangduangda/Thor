# coding:utf-8
from thor.leetcode.linklist.ListNode import ListNode


class Solution(object):
	"""
		给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
		请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性
	"""

	def oddEvenList(self, head: ListNode) -> ListNode:
		"""
			可参考ac_083
		:param head:
		:return:
		"""
		if not head or not head.next:
			return head
		odd = head
		even = head.next
		p = even
		while even and even.next:
			odd.next = even.next
			odd = odd.next
			even.next = odd.next
			even = even.next
		odd.next = p
		return head
