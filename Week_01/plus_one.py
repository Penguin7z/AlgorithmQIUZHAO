# -*- coding: utf-8 -*-

# 加一

# 思路总结
# 重点是最后一位加完之后是否要进位。如果要进位，其实又是一次加一操作，和操作最后一位的思路一样


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                return digits

            digits[i] = digits[i] % 10
            i -= 1

        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    s = Solution()

    print s.plusOne([1, 2, 3, 4]) == [1, 2, 3, 5]

    print s.plusOne([]) == [1]

    print s.plusOne([1, 2, 3, 9]) == [1, 2, 4, 0]

    print s.plusOne([9, 9, 9]) == [1, 0, 0, 0]

