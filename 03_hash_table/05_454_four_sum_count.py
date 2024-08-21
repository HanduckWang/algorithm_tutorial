# 四数相加，四个独立数组，不用考虑有重复的四个元素相加等于0的情况，哈希法典型题目
# 与其他两、三、四数之和，2可哈希（要返回索引下标，不能排序因此不可双指针），34不能哈希，因为题目要求不能包含重复三元组，还需去重容易超时，直接使用双指针（要排序）
class Solution:
    def four_sum_count(self, num1: list[int], num2: list[int], num3: list[int], num4: list[int]) -> int:
        table = {}

        for i1 in num1:
            for i2 in num2:
                sum1 = i1 + i2
                table[sum1] = table.get(sum1, 0) + 1

        count = 0
        for i3 in num3:
            for i4 in num4:
                sum2 = -i3 - i4
                if sum2 in table:
                    count += table[sum2]

        return count

