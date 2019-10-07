# coding: utf-8
from thor.leetcode.linklist.ListNode import ListNode

"""
	使用双指针法解题。设置两个指针，first,second，先另first指针从头结点开始移动n位，
	然后让second指向head,first,second同时开始向后移动，如果first.next为空，说明
	到达链表尾部， 则此时second.next为要删除掉的节点。特殊情况，如果要删除的节点刚好
	是头结点，需要做另外的判断
"""


class Solution(object):
	"""
		删除链表倒数第n个节点
	"""

	def removeNthElement(self, head: ListNode, n):
		if not head:
			return head
		first = head
		second = head
		while n != 0:
			first = first.next
			n -= 1
		
		if not first:
			return head.next
		while first.next:
			second = second.next
			first = first.next
		second.next = second.next.next
		return head
