# -*- coding: utf-8 -*-

# 删除排序数组中的重复项

# 思路总结
# 双指针移动法，一个指针记录遍历的位置，一个指针记录新值被占用到哪个位置了。


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                l += 1
            nums[l] = nums[i]
        return 0 if not nums else l + 1


if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([0]) == 1
    print s.removeDuplicates([0, 0]) == 1
    print s.removeDuplicates([0, 1]) == 2
    print s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
