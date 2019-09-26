# coding:utf-8


from thor.leetcode.linklist.ListNode import ListNode


class Solution(object):
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return head

		cur = head
		while cur and cur.next:
			if cur.val == cur.next.val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head
