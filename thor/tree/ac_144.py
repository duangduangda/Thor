# ！ /usr/bin/env pythonm
from thor.tree import TreeNode


class Solution(object):
	def preorder_travelsal(self, root: TreeNode) -> [int]:
		if not root:
			return []
		else:
			return [root.val] + self.preorder_travelsal(root.left) + self.preorder_travelsal(root.right)
