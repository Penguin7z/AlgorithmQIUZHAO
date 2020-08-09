# -*- coding: utf-8 -*-

# 最小路径和

# 思路总结
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 动态规划，因为只能从左右往右，或从上往下移动，那么分别考虑到达每一个点时的最小值，接下来就是从新的点往目标点求最小值了。
# 路途的记忆，可以直接修改grid，把每个节点的最小值覆盖，节约空间消耗。
# 额外需要注意的是处理好边界条件的判断和边界值的处理。


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print s.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]) == 7
