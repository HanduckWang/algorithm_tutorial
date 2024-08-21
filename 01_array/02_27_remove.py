class Solution:
    def remove(self, nums: list[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):

            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow  # 注意return的内容
