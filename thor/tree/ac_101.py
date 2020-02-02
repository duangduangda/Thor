# ！ /usr/bin/env python
from thor.tree import TreeNode


class Solution(object):
	'''
		1. 都为空指针返回True
		2. 只有一个为空返回False
		3. 递归过程
			a. 判断两个指针是否相等
			b. 判断A左子树和B右子树是否对称
			c. 判断A右子树和B左子树是否对称
	'''

	def is_symmetric(self, root: TreeNode):
		if not root:
			return True
		else:
			self.func(root.left, root.right)

	def func(self, p: TreeNode, q: TreeNode):
		if not p and not q:
			return True
		elif p and q and p.val == q.val:
			return self.func(p.left, q.right) and self.func(p.right, q.left)
		else:
			return False
