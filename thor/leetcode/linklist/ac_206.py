# coding:utf-8
from thor.leetcode.linklist.ListNode import ListNode


class Solution(object):
	"""
	反转链表
	"""

	def reverse_list(self, head: ListNode):
		if not head:
			return head
		pre = None
		while head.next:
			cur = head.next
			head.next = pre
			pre = head
			head = cur
		head.next = pre
		return head


def main():
	first = ListNode(1)
	second = ListNode(3)
	third = ListNode(2)
	first.next = second
	second.next = third
	first.travel()


if __name__ == '__main__':
	main()
