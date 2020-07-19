# -*- coding: utf-8 -*-

#

# 思路总结
# 无非就是两个指针各指一个数组，各去一个值比较大小。
# 但是小技巧就是：从后往前遍历，后面的都是最大的数字，已经可以确定好仍在最后。所以不需要额外空间。


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, l = m - 1, n - 1, m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[l] = nums2[l2]
                l2 -= 1
            else:
                nums1[l] = nums1[l1]
                l1 -= 1

            l -= 1

        if l2 > 0:
            nums1[:l2 + 1] = nums2[:l2 + 1]


if __name__ == "__main__":
    s = Solution()


