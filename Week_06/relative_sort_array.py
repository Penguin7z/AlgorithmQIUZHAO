# -*- coding: utf-8 -*-

from collections import Counter

# 数组的相对排序

# 思路总结
# 首先构建一个hash count结构，然后遍历，构建数组。最后再把没出现在arr2中的排序好，拼接到最后。


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = dict(Counter(arr1).most_common())
        res = []
        for x in arr2:
            res += [x] * d.get(x, 0)

        extra_list = [x for x in arr1 if x not in arr2]
        extra_list = sorted(extra_list)
        return res + extra_list


if __name__ == "__main__":
    s = Solution()
    print s.relativeSortArray(
        arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
        arr2=[2, 1, 4, 3, 9, 6])
