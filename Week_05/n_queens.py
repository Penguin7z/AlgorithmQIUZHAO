# -*- coding: utf-8 -*-

# N皇后

# 思路总结
# DFS
# 存储几个中间变量，已经放置的皇后，对角线位置


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.dfs([], n, result, [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in line] for line in result]

    def dfs(self, queens, n, result, xy1, xy2):
        p = len(queens)
        if p == n:
            result.append(queens)
            return

        for q in range(n):
            if q not in queens and p-q not in xy1 and p+q not in xy2:
                self.dfs(queens+[q], n, result, xy1+[p-q], xy2+[p+q])


if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)

