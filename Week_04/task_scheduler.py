# -*- coding: utf-8 -*-

# 任务调度器

# 思路总结
# 因为相同任务执行之前必须间隔n个时间，那么优先执行任务数最多的任务，然后依次插入其他任务，占位。
# res = (freq_A-1) * (n+1) + p，p 等于和 A 出现次数一致的数目

from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        most = Counter(tasks).most_common()
        most_freq, most_n = most[0][1], 1
        for i in range(1, len(most)):
            if most[i][1] == most_freq:
                most_n += 1
        res = (most_freq - 1) * (n + 1) + most_n
        return max(res, len(tasks))


if __name__ == "__main__":
    s = Solution()
    print s.leastInterval(["A","A","A","B","B","B"], 2)
    print s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)

