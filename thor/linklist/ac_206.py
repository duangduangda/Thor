# coding:utf-8
from thor.linklist.ListNode import ListNode


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
	head = ListNode(1).append(3).append(2)
	head.travel()
	s = Solution()
	s.reverse_list(head).travel()


if __name__ == '__main__':
	main()
