# -*- coding: utf-8 -*-

# 买卖股票的最佳时机 II

# 思路总结
# 贪心法。从第一天开始，永远取最小时间段内的最高利润。大于0，就假设前一天买了，小于0就当前一天没买。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit, start = 0, prices[0]
        for i in range(1, len(prices)):
            if start < prices[i]:
                profit += prices[i] - start
                start = prices[i]
            else:
                start = prices[i]

        return profit


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    print s.maxProfit([1, 2, 3, 4, 5, 6]) == 5
    print s.maxProfit([6, 5, 4, 3, 2, 1]) == 0
