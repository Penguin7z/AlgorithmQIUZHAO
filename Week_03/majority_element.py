# -*- coding: utf-8 -*-

# 多数元素

# 思路总结
# 1. hash存储每一个数字出现的次数，出现超过一半的时候，就得出结果了。此处考虑for循环提前退出条件可减少遍历次数。hash的最大长度逻辑上为数组长度的一半以下。
# 所以需要额外存储n/2
# 2. 利用数学逻辑，超过一半，那么如果数组有序的话，最中间一位必然为出现次数多的数，因为它超过一半了。
# 3.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sorted(nums)[len(nums)/2]

        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > len(nums) / 2:
                return num


if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([2, 2, 3]) == 2
    print s.majorityElement([2, 2]) == 2
    print s.majorityElement([2, 3, 4, 5, 4, 4, 4]) == 4

