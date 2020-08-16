# -*- coding: utf-8 -*-

# 比特位计数

# 思路总结
# 二进制，高位每多一个1，就是翻了1倍。所以，一个二进制数有多少个1，和它其他位都不变的情况下，左移1位是有关系的。所以我们可以反着看
# 把从高位到低位倒数第二位看做相同的，然后看最低位，最低位无非是0和1，那么就是加0个1或者1个1。由此可见，是存在重复计算的。
# 那么我们一开始从比较少的位数算起，后面的计算就都是在利用之前算好的值，再加上最低位的结果了。
# 提前申请返回值内存，避免数组空间不够 append 操作引发的搬运消耗。


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[(i >> 1)] + (i & 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.countBits(2)
    print s.countBits(5)
    print s.countBits(10)

