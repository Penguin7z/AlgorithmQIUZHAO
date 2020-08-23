# -*- coding: utf-8 -*-

# 反转字符串中的单词 III

# 思路总结
# 根据空格，分割字符串成单词列表，然后分别反转每一个单词


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)


if __name__ == "__main__":
    ss = Solution()
    print ss.reverseWords("Let's take LeetCode contest")

