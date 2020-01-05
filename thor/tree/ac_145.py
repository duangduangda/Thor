#! /usr/bin/env python
import TreeNode


class Solution(object):
    def postorder_traversal(self, root: TreeNode):
        if not root:
            return []
        else:
            return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]
