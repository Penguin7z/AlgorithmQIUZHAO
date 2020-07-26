# -*- coding: utf-8 -*-

# 组合

# 思路总结
# 和排列题类似，不同的是：排列是每一组的个数和总数相等。这里是子集。
# 如果用排列的题解方法的来实现的话，则2个地方需要变更：
# 1. 判断路径长度==k，则可以加入有效序列
# 2. 重复怎么办？比较输入的一点是：给的是n，则可以认为数组有序。数组有序，则可以从左往右移动。每次index+1，然后取K个。则避免的重复问题。


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], range(1, n+1), k, 0)
        return res

    def dfs(self, res, path, nums, k, index):
        if len(path) == k:
            res.append(path)
        for i in range(index, len(nums)):
            # path + [nums[i]] 是个小技巧
            self.dfs(res, path + [nums[i]], nums, k, i+1)


if __name__ == "__main__":
    s = Solution()

