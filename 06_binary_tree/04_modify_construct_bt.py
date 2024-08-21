from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 6.翻转二叉树
    def invert_bt(self, root:TreeNode) -> TreeNode:
        if not root:
            return None
        # 前序和后序都易
        root.left, root.right = root.right, root.left
        self.invert_bt(root.left)
        self.invert_bt(root.right)
        return root
    
    def invert_bt_iteration(self, root:TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if root.left:
                stack.append(node.left)
            if root.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
    # 18. 中前序遍历序列构造二叉树、中后遍历序列构造二叉树（必须有中序，否则不唯一）
    # 凡是构造二叉树类的题目，都要使用前序遍历
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 一、特殊情况讨论：树为空，或者说递归终止
        if not preorder:
            return None
        # 二、前序遍历的第一个就是当前的中间节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 三、找（中序）切割点
        separator_idx = inorder.index(root.val)

        # 四、切割inorder数组，得到inorder数组左、右半边，注意区间边界（本处用的左闭右开）
        # 重要：一定先切中序数组
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 五、切割preorder数组，得到preorder数组左、右半边
        # 重要：中序数组大小一定跟前序数组大小相同，用此做切割
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # 六、递归
        root.left = self.build_tree(preorder_left, inorder_left)
        root.right = self.build_tree(preorder_right, inorder_right)
        # 七、返回
        return root
    
    # 19.最大二叉树
    def constructMaximumBinaryTree(self, nums: List[int]):
        if not nums:
            return None

        maxValueIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maxValueIndex]:
                maxValueIndex = i

        root = TreeNode(nums[maxValueIndex])

        # 递归地构建左子树和右子树
        root.left = self.constructMaximumBinaryTree(nums[:maxValueIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxValueIndex+1:])

        return root
    

    # 21.合并二叉树，前中后序都可，优先前序
    def merge_trees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left=self.merge_trees(root1.left, root2.left)
        root1.right=self.merge_trees(root1.right, root2.right)
        return root1