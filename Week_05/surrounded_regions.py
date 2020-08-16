# -*- coding: utf-8 -*-

# 被围绕的区域

# 思路总结
# bfs 递归
# bfs 非递归，一般用队列存储
# dfs 递归
# dfs 非递归，一般用 stack
# 只需要从周围一圈，找到O，顺着O往内圈找，这些是都连通的。这些和边界连通的做特殊标记。
# 全部遍历完之后，再把未被特殊标记的全部变成X，把特殊标记的恢复成O


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0:
            return board
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == "O":
                        self.dfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        return board

    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "#"
            self.dfs(board, i + 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j - 1)


if __name__ == "__main__":
    s = Solution()
    """
    x o x
    o x o
    x o x
    
    """
    print s.solve([])
    print s.solve([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])
    print s.solve(
        [["O", "X", "X", "X", "X"], ["X", "O", "O", "X", "X"], ["X", "X", "O", "X", "X"], ["X", "O", "X", "X", "X"]])
