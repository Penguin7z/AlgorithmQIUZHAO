# -*- coding: utf-8 -*-

# 移动零

# 思路总结
# 利用快慢指针，一个遍历数组，一个记录当前非0位置到达的数组下标。


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for index, v in enumerate(nums):
            if v != 0:
                if left != index:
                    nums[left] = v
                    nums[index] = 0
                left += 1


if __name__ == "__main__":
    s = Solution()
    data = [0, 1, 0, 3, 12]
    s.moveZeroes(data)
    print data == [1, 3, 12, 0, 0]

    data = [0]
    s.moveZeroes(data)
    print data == [0]

    data = [1]
    s.moveZeroes(data)
    print data == [1]

    data = [0, 0, 1]
    s.moveZeroes(data)
    print data == [1, 0, 0]
