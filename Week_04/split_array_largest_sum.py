# -*- coding: utf-8 -*-

# 分割数组的最大值

# 思路总结
# 采用二分法，左边是数组最大值，右边是数组总和。然后二分取一个值，找到最小的最大分割子数组和。


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def helper(x):
            total, group = 0, 1
            for num in nums:
                if total + num > x:
                    group += 1
                    if group > m:
                        return False
                    total = num
                else:
                    total += num
            return group <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    s = Solution()
    print s.splitArray([7, 2, 5, 10, 8], 2)
