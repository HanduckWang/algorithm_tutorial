# 求交集
# 随便搞，两个set也行
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        table = {}  # 用于存储nums1中每个数字出现的次数
        res = set()

        # 这里用table本质上是去重
        for num in nums1:
            # 使用 table.get(num, 0) 获取key为num的value在table中的当前计数，如果没有则默认为0。就是通过索引取值，更安全而已
            table[num] = table.get(num, 0) + 1

        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]  # 从字典 table 中删除键 num 及其对应的值，删不删不影响

        return list(res)


