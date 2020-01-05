#! /usr/bin/env python

import TreeNode


class Solution(object):
    '''
        1. 如果都为空指针，返回True
        2. 递归过程
            a. 判断两个指针值是否相等
            b. 判断A左子树与B右子树相等
            c. 判断A右子树与B右子树相等
    '''

    def is_same_tree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        else:
            return False
