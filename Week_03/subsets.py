# -*- coding: utf-8 -*-

# 子集

# 思路总结
# 和全排列思路类似，但是和全排列不一样的是，全排列是每个子集数量一致，且可以打乱顺序重复，子集这个不可以重复。
# 所以关键点在于两个地方：第一，不定长的数量都算，怎么界定不定长。第二，乱序怎么解决。
# 引入了2个新的变量，一个start，也就是开始变量。我们假设每个数被选中了，则下一次选不再是在全数据中选，而是只能在第一个数之和选。
# 以此解决乱序的问题。引入了length变量，每次子集中有几个数的时候，就算完成。


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        for k in range(len(nums)+1):
            self.DFS(res, visited, [], nums, 0, k)
        return res

    def DFS(self, res, visited, path, nums, start, length):
        if len(path) == length:
            res.append(path)
            return
        for i in range(start, len(nums)):
            if i not in visited:
                visited.add(i)
                self.DFS(res, visited, path + [nums[i]], nums, i+1, length)
                visited.remove(i)


if __name__ == "__main__":
    s = Solution()
    print s.subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

