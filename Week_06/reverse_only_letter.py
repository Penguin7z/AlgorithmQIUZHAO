# -*- coding: utf-8 -*-

# 仅仅反转字母

# 思路总结
# 反转，也就是倒过来，栈就是先进后出，符合倒过来。所以把字母扔进去一个栈，再读出来，就完成了反转。


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = [c for c in S if c.isalpha()]
        res = [l.pop() if ch.isalpha() else ch for ch in S]
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    print s.reverseOnlyLetters("a-bC-dEf-ghIj")

