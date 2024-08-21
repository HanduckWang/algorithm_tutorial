class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        char_list = list(s)
        length = len(char_list)
        for i in range(0, length, 2 * k):
                char_list[i:i+k] = char_list[i:i+k][::-1]  # [::-1]切片操作，反转序列
        return ' '.join(char_list)

