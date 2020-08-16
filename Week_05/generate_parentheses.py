# -*- coding: utf-8 -*-

# 括号生成

# 思路总结
# 左右括号数量是相等的，左边可以先用，右边不能先用。
# 右边的括号永远要大于等于左边。
# 严格控制放括号"速度"


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left, right, res = n, n, []
        self.dfs(left, right, "", res)
        return res

    def dfs(self, left, right, path, res):
        if left == 0 and right == 0:
            res.append(path)
            return

        if left > right:
            return

        if left > 0:
            self.dfs(left-1, right, path + "(", res)

        if right > 0:
            self.dfs(left, right-1, path + ")", res)


if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)

