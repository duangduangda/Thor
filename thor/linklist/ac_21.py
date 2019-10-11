# coding:utf-8
from thor.linklist.ListNode import ListNode


class Solution(object):
	def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None:
			return l2
		elif l2 is None:
			return l1
		else:
			head = ListNode(-1)
			p = head

			while l1 is not None and l2 is not None:
				if l1.val <= l2.val:
					p.next = l1
					l1 = l1.next
				else:
					p.next = l2
					l2 = l2.next
				p = p.next
			if l1 is None:
				p.next = l2
			else:
				p.next = l1
			return head.next


def main():
	l1 = ListNode(1).append(2).append(3)
	l2 = ListNode(2).append(4)
	s = Solution()
	l3 = s.mergeTwoList(l1, l2)
	l3.travel()


if __name__ == '__main__':
	main()
