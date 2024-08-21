class Solution:
    def reverse_word(self, s: str):
        # 拆分为单词，转换为list类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left] < words[right]
            left += 1
            right -= 1

        return " ".join(words)

