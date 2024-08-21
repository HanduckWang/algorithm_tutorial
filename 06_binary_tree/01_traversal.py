from types import List
import collections


class TreeNode():
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def recursion_pre(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []

        res.append(root.val)
        self.recursion_pre(root.left)
        self.recursion_pre(root.right)
        
        return res

    def iteration_pre(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node)
            
            if node.left:
                stack.append(node)

        return res


    def recursion_in(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        res = []
        self.recursion_in(root.left)
        res.append(root.val)
        self.recursion_in(root.right)
        return res


    def iteration_in(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = []
        res = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            res.append(node.val)

            node = node.right
        return res


    def recursion_post(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        res = []
        self.recursion_post(root.left)
        self.recursion_post(root.right)
        res.append(root.val)
        return res


    def iteration_post(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
        
        return res[::-1]
    


    def iteration_level(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = collections.deque([root])
        res  = []

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

