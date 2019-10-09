# coding:utf-8
from thor.leetcode.linklist.ListNode import ListNode


class Solution(object):
	"""
		给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
		请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性
	"""

	def oddEvenList(self, head: ListNode) -> ListNode:
		"""
			可参考ac_083,初始设置两个指针，一个指向奇数，一个指向偶数
			然后让奇数的指针连接下一个奇数，偶数指针连接下一个偶数，
			最后将两者进行连接
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
		"""连接奇偶链表"""
		odd.next = p
		return head
