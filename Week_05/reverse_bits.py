# -*- coding: utf-8 -*-

# 颠倒二进制位

# 思路总结
# 按位取，按位放。取n的低位，放到结果值的高位。


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n, power = n >> 1, power - 1
        return res

    # def reverseBits(self, n):
    #     ret, power = 0, 24
    #     cache = dict()
    #     while n:
    #         ret += self.reverseByte(n & 0xff, cache) << power
    #         n = n >> 8
    #         power -= 8
    #     return ret

    # def reverseByte(self, byte, cache):
    #     if byte not in cache:
    #         cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
    #     return cache[byte]

    # def reverseBits(self, n):
    #     n = (n >> 16) | (n << 16)
    #     n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    #     n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    #     n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    #     n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    #     return n


if __name__ == "__main__":
    s = Solution()
    print s.reverseBits(43261596)

