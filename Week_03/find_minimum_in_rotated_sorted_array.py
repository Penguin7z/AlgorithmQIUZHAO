# -*- coding: utf-8 -*-

# 寻找旋转排序数组中的最小值

# 思路总结
# 1. 遍历一遍，找到左侧大于右侧的第一次出现的时刻，则右侧数就是结果。如果遍历完都不存在，那么就是数组第一个元素
# 2. 二分法
# 左>中<右 旋转
# 左<中>右 旋转
# 左<中<右 未旋转
# 左>中>右 不应该发生


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int] 6,7,1,2,3,4,5
        :rtype: int     6,7,8,9,10,1,2,3,4,5
        """
        # if not nums:
        #     return
        #
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return nums[i+1]
        # return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    print s.findMin([1, 2]) == 1
    print s.findMin([6, 7, 1, 2, 3, 4, 5]) == 1
    print s.findMin([6, 7, 8, 9, 10, 11, 4, 5]) == 4
