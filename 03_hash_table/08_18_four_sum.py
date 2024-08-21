# k数之和为t，均同理
class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()
        length = len(nums)

        for i in nums:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in nums:
                if j > 0 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = length - 1

            while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
        return res


