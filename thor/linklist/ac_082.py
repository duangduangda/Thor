# coding:utf-8


from thor.linklist.ListNode import ListNode


class Solution(object):
	"""迭代法，使用哑结点和快慢指针"""

	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head

		dummy = ListNode(-1)
		dummy.next = head
		slow = dummy
		fast = dummy.next
		while fast:
			if fast.next and fast.next.val == fast.val:
				"""如果出现一样的值，先记录下来"""
				temp = fast.val
				"""
					判断后续是否还有一样的值，如果有，指针往后继续移动
					直到到达最后一个值一样的位置
				"""
				while fast and fast.val == temp:
					fast = fast.next
			else:
				"""
					如果之前存在重复，删除掉重复的元素；
					如果未出现重复的，正常移动慢指针
				"""
				slow.next = fast
				slow = fast
				fast = fast.next
			slow.next = fast
			return dummy.next
