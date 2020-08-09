# -*- coding: utf-8 -*-

# 最大正方形

# 思路总结
# 动态规划，首先求面积，也就是求得最大边。求最大边，就是求最大的连续1的正方形。假设一点(i,j)为一个正方形的右下角。
# 那么它的左下角，左上角，右上角分别向外辐射。如果另外三个点都是1，那边边长就是2。然后每个区域内又符合这样的逻辑，
# 右下角，左下角，左上角，右上角，求一个连续边长。
# 最终的边长公式就是：在(i, j)为1时，dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) == 0:
            return 0

        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        max_side = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == "__main__":
    s = Solution()
    print s.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]) == 4

