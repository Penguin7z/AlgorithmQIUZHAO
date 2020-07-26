# -*- coding: utf-8 -*-

# 全排列

# 思路总结
# 典型回溯法，回溯法需要记住：走过的路径，再撤销，返回到上一层，继续走别的分支。
# 所以需要：记住走过的路径，装载可用路径的容器，中间过程的变量
# 小技巧：一条可用路径走到底，需要撤销返回上一层，递归函数也需要deepcopy传输中间变量。可以直接用path + [nums[i]]，
# 取代deepcopy，同时，也不用写撤销方法了。因为根本没append。


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        self.dfs(res, visited, [], nums)
        return res

    def dfs(self, res, visited, path, nums):
        if len(path) == len(nums):
            res.append(path)
            path = []
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                # path + [nums[i]] 是个小技巧
                self.dfs(res, visited, path + [nums[i]], nums)
                visited.remove(i)


if __name__ == "__main__":
    s = Solution()
    print s.permute([1, 2, 3])

