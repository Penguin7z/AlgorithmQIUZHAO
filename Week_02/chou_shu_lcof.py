# -*- coding: utf-8 -*-

# 剑指 Offer 49. 丑数

# 思路总结
# 其实就是快慢指针问题，只不过这是三指针，然后一起往前走，找出最小值。


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        dp, p2, p3, p5 = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                p2 += 1
            if dp[i] == n3:
                p3 += 1
            if dp[i] == n5:
                p5 += 1

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print s.nthUglyNumber(0) == 0
    print s.nthUglyNumber(1) == 1
    print s.nthUglyNumber(10) == 12

