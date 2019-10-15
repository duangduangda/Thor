#  coding:utf-8
from thor.linklist.ListNode import ListNode


class Solution(object):
	"""双指针+哑结点"""

	def rotateRight1(self, head: ListNode, k: int) -> ListNode:
		if head is None or head.next is None or k == 0:
			return head
		else:
			dummy = ListNode(-1)
			dummy.next = head
			first = dummy
			second = dummy
			length = 0
			"""移动至尾部结点"""
			while first.next:
				first = first.next
				length += 1

			"""转化为单圈"""
			k %= length
			for i in range(length - k):
				second = second.next

			"""执行旋转操作"""
			first.next = dummy.next
			dummy.next = second.next
			second.next = None

			return dummy.next

	"""单指针"""

	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head or not head.next or k == 0:
			return head
		else:
			p = head
			length = 1
			while p.next:
				p = p.next
				length += 1
			k %= length
			"""成环"""
			p.next = head
			for i in range(length - k):
				p = p.next
			head = p.next
			p.next = None
			return head


def main():
	s = Solution()
	l1 = ListNode(1).append(2).append(3).append(4).append(5)
	s.rotateRight(l1, 2).travel()

	l2 = ListNode(0).append(1).append(2)
	s.rotateRight(l2, 4).travel()


if __name__ == '__main__':
	main()
