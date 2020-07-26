# -*- coding: utf-8 -*-

# N叉树的后序遍历

# 思路总结
# 相比较于二叉树后序遍历，需要先把children遍历完。

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            for child in root.children:
                self.dfs(child, res)
            res.append(root.val)
        return res


if __name__ == "__main__":
    s = Solution()
