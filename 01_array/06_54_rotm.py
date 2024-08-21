# class Solution:
#     def rotationmatrix(self, matrix: list[list[int]]) -> list[int]:
#         new_list = []
#         x, y = 0, 0
#         m, n = len(matrix), len(matrix[0])
#         offset = 1
#         while m-offset and n-offset > 0:
#             for i in range(y, n-offset):
#                new_list.append(matrix[x][i])
#             for i in range(x, m-offset):
#                 new_list.append(matrix[i][n-offset])
#             if x<n and y<m:
#                 for i in range(n-offset, y, -1):
#                     new_list.append(matrix[m-offset][i])
#                 for i in range(m-offset, x, -1):
#                     new_list.append(matrix[i][y])
#             x += 1              y += 1
#             offset += 1
#         return new_list
class Solution:

    def rotationmatrix(self, matrix: list[list[int]]) -> list[int]:
        new_list = []
        if not matrix or not matrix[0]:  # 如果matrix为空或者第一行为空（二者不重复）返回
            return new_list

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1  # 行列和numpy取法不同

        while left <= right and top <= bottom:
            # 从左到右遍历上层
            for i in range(left, right):  # 四for边界条件自己把控，要么全部前开后闭要么全闭
                new_list.append(matrix[top][i])
            # 从上到下遍历右侧
            for i in range(top, bottom + 1):
                new_list.append(matrix[i][right])
            if top < bottom and left < right:  # 避免到中心区域（最后一次）对元素重复添加，确保只有当还有超过一行或一列的元素时才进行从右到左和从下到上的遍历
                # 从右到左遍历下层
                for i in range(right - 1, left, -1):
                    new_list.append(matrix[bottom][i])
                # 从下到上遍历左侧
                for i in range(bottom, top, -1):
                    new_list.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return new_list

# better
    def rotationmatrix(self, matrix: list[list[int]]) -> list[int]:
        new_list = []
        if not matrix or not matrix[0]:  # 如果matrix为空或者第一行为空（二者不重复）返回
            return new_list

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1  # 行列和numpy取法不同

        while left <= right and top <= bottom:   # 此处有等号，未必是方阵，中间
            # 从左到右遍历上层
            for i in range(left, right):  # 四for边界条件自己把控，要么全部前开后闭要么全闭
                new_list.append(matrix[top][i])
            # 从上到下遍历右侧
            for i in range(top, bottom):
                new_list.append(matrix[i][right])
                # 从右到左遍历下层
            for i in range(right, left, -1):
                new_list.append(matrix[bottom][i])
            # 从下到上遍历左侧
            for i in range(bottom, top, -1):
                new_list.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        # 如果是奇数行列的矩阵，最后一圈只有一个元素
        if left == right and top == bottom:
            new_list.append(matrix[top][left])


        return new_list


if __name__ == '__main__':
    solution = Solution()
    matrix = [[9, 7, 5], [7, 8, 9], [4, 5, 6], [6, 9, 4]]
    new = solution.rotationmatrix(matrix)
    print(new, len(new))