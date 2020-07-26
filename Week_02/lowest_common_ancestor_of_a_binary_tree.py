# -*- coding: utf-8 -*-

# 二叉树的最近公共祖先

# 思路总结
# 首先要明确：判定条件。后续DFS遍历，
# 当左右同时为空，不存在；
# 当左不为空，右为空，去左边找；
# 当右不为空，左为空，去右边找；
# 当左右都不为空时，则为root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


if __name__ == "__main__":
    s = Solution()
    node_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    for val in node_list:
        node = TreeNode(val)

    node_list = [TreeNode(x) if x else None for x in node_list]
    print s.lowestCommonAncestor(node_list[0], node_list[9], node_list[10])
