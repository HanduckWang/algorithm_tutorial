from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 29.二叉搜索树中的插入操作
    # 关键理解：在二叉搜索树中插入任何一个节点，都可以在叶子结点找到它的位置
    def insert_into_bst(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            node = TreeNode(val)
            return node
        
        if val < root.val:
            self.insert_into_bst(root.left, val)
        if val > root.val:
            self.insert_into_bst(root.right, val)
        
        return root


    # 30.删除二叉搜索树中的节点
    # 1+5种情况，涉及到重新构造二叉树，中左右
    def delete_node(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:  # 没找到删除节点，返回空
            return root
        if root.val == key:  # 找到删除节点
            if root.left is None and root.right is None:  # 该节点左右孩子为空，直接删除即返回none
                return None
            elif root.left is None:  # 该节点左孩子为空，右不为空，右补位
                return root.right
            elif root.right is None:  # 该节点有孩子为空，左不为空，左补位
                return root.left
            else:  # 左右不为空，被删除节点的左孩子放到其右孩子最左节点上（非右孩子的左孩子，是左叶子）
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left  # 使cur的左指向root的左
                return root.right

        if root.val > key:
            root.left = self.delete_node(root.left, key)
        if root.val < key:
            root.right = self.delete_node(root.right, key)
        return root

    # 31.修剪二叉搜索树
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        
        # 寻找符合区间 [low, high] 的节点
        if root.val < low:
            return self.trim_bst(root.right, low, high)
        if root.val > high:
            return self.trim_bst(root.left, low, high)
        
        # root.left 接入符合条件的左右孩子
        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)
        return root
    
    
    # 32.将有序数组转换为二叉搜索树
    def trave(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.trave(nums, left, mid - 1)
        root.right = self.trave(nums, mid + 1, right)

    def sortedarray_to_bst(self, nums: List[int]) -> TreeNode:
        root = self.trave(nums, 0, len(nums) - 1)
        return root