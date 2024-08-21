class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        records = dict()  # 等价records = {}创建空字典

        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]  # 返回一个列表，即两个数的下标
            records[value] = index
        return []