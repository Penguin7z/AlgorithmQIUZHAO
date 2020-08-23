# -*- coding: utf-8 -*-

from collections import Counter

# 字符串中的第一个唯一字符

# 思路总结
# 唯一一个字符，说明必须得遍历完数组，count是1的，且是第一次出现的。


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict(Counter(s).most_common())
        for i, ch in enumerate(s):
            if d.get(ch, 0) == 1:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    print s.firstUniqChar(s="loveleetcode")

