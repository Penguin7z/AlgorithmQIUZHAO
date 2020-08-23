# -*- coding: utf-8 -*-

# 最长上升子序列

# 思路总结
# 维护一个最长升序数组，数组的长度即为最长上升子序列的长度。从左往右遍历nums，如果新遍历的数字小于升序数组的最大的，
# 则把这个数字插入到升序对组对应的位置，最后比较历史中最大的长度即可。


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        count = 0
        for num in nums:
            left, right = 0, count
            while left < right:
                m = (left + right) >> 1
                if tails[m] < num:
                    left = m + 1
                else:
                    right = m
            tails[left] = num
            count = max(left + 1, count)
        return count


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLIS([9, 2, 7, 4, 1, 5, 2, 6])

