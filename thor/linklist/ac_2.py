# coding:utf-8
from thor.linklist.ListNode import ListNode


class Solution(object):
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None:
			return l2
		elif l2 is None:
			return l1
		else:
			head = ListNode(-1)
			p = head
			temp = 0
			while l1 is not None or l2 is not None:
				if l1 is not None:
					temp += l1.val
					l1 = l1.next
				if l2 is not None:
					temp += l2.val
					l2 = l2.next
				p.next = ListNode(temp % 10)
				p = p.next
				"""进位处理"""
				temp //= 10

			if temp:
				p.next = ListNode(temp)
			return head.next


def main():
	s = Solution()

	l1 = ListNode(2).append(4).append(3)
	l1.travel()
	l2 = ListNode(5).append(6).append(4)
	l2.travel()
	l3 = s.addTwoNumbers(l1, l2)
	print("--" * 3)
	l3.travel()
	print()
	l4 = ListNode(5)
	l4.travel()
	l5 = ListNode(6)
	l5.travel()
	l6 = s.addTwoNumbers(l4, l5)
	print("--" * 3)
	l6.travel()

	print()
	l7 = ListNode(4)
	l7.travel()
	l8 = ListNode(6).append(2)
	l8.travel()
	l9 = s.addTwoNumbers(l7, l8)
	print("--" * 3)
	l9.travel()

	print()
	l10 = ListNode(9).append(9)
	l10.travel()
	l11 = ListNode(9)
	l11.travel()
	print("--" * 3)
	l12 = s.addTwoNumbers(l10, l11)
	l12.travel()


if __name__ == '__main__':
	main()
