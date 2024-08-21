class Solution:
    def rotmatrix(self, n: int) -> list[int]:
        nums = [[0] * n for _ in range(n)]  # 不使用numpy使用列表推导式创建矩阵
        startx, starty = 0, 0
        loop, mid = n // 2, n//2
#         count = 1
#         offset = 1
#         while loop > 0:
#             for i in range(starty, n-offset):
#                 nums[startx][i] = count
#                 count += 1
#             for i in range(startx, n-offset):
#                 nums[i][n-offset] = count
#                 count += 1
#             for i in range(n-offset, starty, -1):
#                 nums[n-offset][i] = count
#                 count += 1
#             for i in range(n-offset, startx, -1):
#                 nums[i][starty] = count
#                 count += 1
#
#             startx += 1
#             starty += 1
#         if n % 2 != 0:
#             nums[mid][mid] = count
#
#         loop -= 1
#         return nums


class Solution:

    def rotmatrix(self, n: int) -> list[int]:
        matrix = [[100] * n for _ in range(n)]

        left, right, top, bottom = 0, n - 1, 0, n - 1  # 行列和numpy取法不同
        count = 1
        while left <= right and top <= bottom:
            # 从左到右遍历上层
            for i in range(left, right):  # 四for边界条件自己把控，要么全部前开后闭要么全闭
                matrix[top][i] = count
                count += 1
            # 从上到下遍历右侧
            for i in range(top, bottom + 1):
                matrix[i][right] = count
                count += 1
            if top < bottom and left < right:  # 为了避免重复遍历，比如n为奇数时，最后一圈只有一个元素，这时候不需要重复遍历
                # 从右到左遍历下层
                for i in range(right - 1, left, -1):
                    matrix[bottom][i] = count
                    count += 1
                # 从下到上遍历左侧
                for i in range(bottom, top, -1):
                    matrix[i][left] = count
                    count += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1  # 有点像递归的思想

        return matrix


# better
    def rotmatrix(self, n: int) -> list[int]:
        matrix = [[100] * n for _ in range(n)]

        left, right, top, bottom = 0, n - 1, 0, n - 1  # 行列和numpy取法不同
        count = 1
        while left < right and top < bottom:  # 此处无等号，方阵，靠缩圈，中间必然单独剩一个
            # 从左到右遍历上层
            for i in range(left, right):  # 四for边界条件自己把控，要么全部前开后闭要么全闭
                matrix[top][i] = count
                count += 1
            # 从上到下遍历右侧
            for i in range(top, bottom):
                matrix[i][right] = count
                count += 1

            # 从右到左遍历下层
            for i in range(right, left, -1):
                matrix[bottom][i] = count
                count += 1
            # 从下到上遍历左侧
            for i in range(bottom, top, -1):
                matrix[i][left] = count
                count += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        if left == right and top == bottom:
            matrix[top][left] = count

        return matrix


if __name__ == '__main__':
    solution = Solution()
    result = solution.rotmatrix(4)
    print(result, len(result))


