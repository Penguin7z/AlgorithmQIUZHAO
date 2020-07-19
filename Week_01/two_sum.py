# -*- coding: utf-8 -*-

# 两数之和

# 思路总结
# 1. 暴力解决，2重循环；
# 2. 既然用到2重循环，不如先排序，排序时间复杂度小于2重循环。然后2重循环也可以得到优化，比如二分法寻找值
# 3. 既然都有二分法了，那不就变成寻找某个值了吗？那就用两次单循环遍历，第一次单循环写入一个字典，需要那些值，第二次遍历看字典里面有没有需要的值。
# 4. 既然两次单层循环，那有没有办法变成一次单层循环呢？嗯，可以一边遍历一边塞值到map对象里面。因为，前面就算没有，后面相减之后的值还会再需要前面的数值的。所以不矛盾。


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in d:
                return [d[left], i]
            else:
                d[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9) == [0, 1]

    print s.twoSum([2, 7, 11, 15], 10) == []

    print s.twoSum([], 10) == []

    print s.twoSum([1], 10) == []

    print s.twoSum([1, 2], 10) == []

    print s.twoSum([1, 9], 10) == [0, 1]

    print s.twoSum([0, 10], 10) == [0, 1]

