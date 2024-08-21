# 加了双指针，把n^3复杂度降到n^2
class Solution:
    def three_sum(self, nums: list[int]) -> int:
        res = []
        nums.sort()
        nums_length = len(nums)

        for i in range(nums_length):
            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i - 1]:  # 去重操作
                continue

            left = i + 1
            right = nums_length - 1

            while right > left:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 下面的代码放在相等时候的else模块，缩小区间
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1

        return res