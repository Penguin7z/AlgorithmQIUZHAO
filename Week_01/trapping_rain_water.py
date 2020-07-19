# -*- coding: utf-8 -*-

# 接雨水

# 思路总结
# 双指针法，一左一右进行移动。没遇到一个低点，加入中间都没有柱子了，则至少可以接低点的水量。
# 然后再具体到一边，水量就是历史最高减新出现的低点。也就是说，左边是历史最高-往右移动出现的新的低点。右侧反之


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        area = 0

        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                area += max_left - height[left]
                left += 1
            else:
                area += max_right - height[right]
                right -= 1

        return area


if __name__ == "__main__":
    s = Solution()
    print s.trap([]) == 0
    print s.trap([1]) == 0
    print s.trap([1, 1]) == 0
    print s.trap([1, 2]) == 0
    print s.trap([2, 1, 2]) == 1
    print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
