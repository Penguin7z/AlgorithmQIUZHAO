# -*- coding: utf-8 -*-

# 最小基因变化

# 思路总结
# 从某个字符串变成另一个字符串，只到变成目标字符串，典型解决方案就是DFS和BFS。
# BFS的思路是把当前的字符串能变成的下个合法的字符串都列出来，只到里面有目标字符串，结束。


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank:
            return -1

        q = [(start, start, 0)]
        while q:
            current, previous, step = q.pop(0)
            if current == end:
                return step

            for new_str in bank:
                if self.valid_change(current, new_str) and new_str != previous:
                    q.append((new_str, current, step + 1))

        return -1

    def valid_change(self, start, end):
        change_count = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                change_count += 1
        return change_count == 1


if __name__ == "__main__":
    s = Solution()
    print s.minMutation(start="AACCGGTT", end="AACCGGTA", bank=["AACCGGTA"])
    print s.minMutation(start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    print s.minMutation(start="AAAAACCC", end="AACCCCCC", bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"])

