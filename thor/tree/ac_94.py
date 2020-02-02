#! /usr/bin/env python
from thor.tree import TreeNode


class Solution(object):
	def inorder_traversal(self, root: TreeNode):
		if not root:
			return []
		else:
			return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
