# -*- coding: utf-8 -*-

# 编辑距离

# 思路总结
# 动态规划
# word1到word2，有三种操作，插入，删除，替换。
# 定义dp[i][j]为word1到i位置转化为word2到j位置的最小步数，
# 抽象三种操作：dp[i-1][j-1]为替换，dp[i-1][j]为删除，dp[i][j-1] 为插入操作
# 那么则可以得到：
# dp[i][j] = dp[i-1][j-1]，当word1[i] == word2[j]
# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，当word1[i] != word2[j]


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] + 1

        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print s.minDistance("horse", "ros")
    print s.minDistance("intention", "execution")

