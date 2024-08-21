class Solution:
    def square(self, nums: list[int]) -> list[int]:
        left, right, res_i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums)  # 也可以定义为空列表来存储result
        while left <= right :  # 注意此处为≤否则有个元素取不到
            if nums[left] ** 2 <= nums[right] ** 2:
                res[res_i] = nums[right] ** 2
                right -= 1

            else:
                res[res_i] = nums[left]**2
                left -= 1
            res_i += 1
        return res




