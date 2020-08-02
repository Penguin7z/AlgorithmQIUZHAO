# -*- coding: utf-8 -*-

# Pow(x, n)

# 思路总结
# 1. 高位的n不断拆解成低位的，拆成2的次幂可以利用位运算。如果能整除2拆解，则正好，不能，则需要再额外加乘以x
# 当n为计数，先把结果多乘以x，然后就回归整除偶数n的计算了
# 向下整除 n / 2 等价于 右移一位 n >> 1
# 取余数 n % 2 等价于 判断二进制最右位 n & 1


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -1 * n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print s.myPow(2.00, 0) == 1
    print s.myPow(0.00, 10) == 0
    print s.myPow(2.00, 10) == 1024
    print s.myPow(2.00, -2) == 0.25
    print s.myPow(2.00, 2) == 4

