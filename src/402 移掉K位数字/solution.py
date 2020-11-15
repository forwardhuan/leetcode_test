#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
#
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
# 输入: num = "1432219", k = 3
# 输出: "1219"

# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        count = 0
        index = 0
        temp = list(num)
        while count < k:
            # print(index, " ", temp, ' ', count, k)
            next_index = index + 1
            if next_index == len(temp) or temp[index] > temp[next_index]:
                temp.pop(index)
                index = index - 1
                if index < 0:
                    index = 0
                count = count + 1
            else:
                index = index + 1

        while len(temp) > 1 and temp[0] == '0':
            temp.pop(0)
        return ''.join(temp)


solution = Solution()
solution.removeKdigits('1234', 3)
