# nums = [1, 5, 7, 9, 6, 4]
# target = 6
#
# i = 0
# j = len(nums)
#
# while i<=j:
#     m = (i + j)/2
#     if nums[m]<target:
#         j = m - 1
#     if nums[m]>target:
#         i = m + 1
#     else:
#         return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:  # 注意此处在冒号前
        left, right = 0, len(nums) - 1  # 注意此处为-1
        # middle = left + (right - left) // 2  应该放循环，循环外为初值，需要变化的都在里

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle - 1  # 思考写，不重要和下面写反
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

# 还需要注意第一个我while的判断等号，与+-1的问题，取决于是[]还是[)
