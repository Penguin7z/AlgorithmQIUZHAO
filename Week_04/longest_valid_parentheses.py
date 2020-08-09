# -*- coding: utf-8 -*-

# 最长有效括号

# 思路总结
# 1. 栈 2. DP
# 栈的话一个小技巧是默认塞进去一个"）"


class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        stack, result = [(-1, ")")], 0
        for i in range(len(s)):
            if s[i] == ")" and stack[-1][1] == "(":
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack.append((i, s[i]))

        return result


if __name__ == "__main__":
    s = Solution()
    print s.longestValidParentheses(")(()()())")
    print s.longestValidParentheses("())")
    print s.longestValidParentheses("()(()")
    print s.longestValidParentheses(")()())")
    print s.longestValidParentheses("()()")

