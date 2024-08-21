class Solution:
    def minlen(self, s: int, nums: list[int]) -> int:
        left, right, length = 0, 0, len(nums)  # 单独定义length避免循环中重复调用len并增加可读性，是个好习惯
        min_len = float('inf')
        cur_sum = []

        while right < length:  # 注意边界条件
            cur_sum += nums[right]

            while cur_sum > s:
                min_len = min(min_len, right - left + 1)  # 更新最短数组长度
                cur_sum -= nums[left]
                left += 1

            right += 1
        return min_len if min_len != float('inf') else 0

